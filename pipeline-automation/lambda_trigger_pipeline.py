"""
trigger-retail-pipeline
------------------------
Lambda function triggered by S3 "ObjectCreated" events on the
raw/orders/ prefix. Starts the Glue ETL job (retail-transform-orders)
so a new file landing in the raw zone automatically kicks off the
transform -> curated pipeline.

Paste this whole file into the Lambda console's code editor
(Step 9 of the AWS console guide), then click Deploy.
"""

import json
import logging

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

GLUE_JOB_NAME = "retail-transform-orders"

glue_client = boto3.client("glue")


def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))

    # Pull out which file triggered this, purely for logging/debugging —
    # the Glue job itself re-reads the whole raw table via the crawler
    # catalog, so we don't need to pass the specific key into the job.
    triggered_by = []
    for record in event.get("Records", []):
        bucket = record.get("s3", {}).get("bucket", {}).get("name", "unknown-bucket")
        key = record.get("s3", {}).get("object", {}).get("key", "unknown-key")
        triggered_by.append(f"s3://{bucket}/{key}")
        logger.info("New object detected: s3://%s/%s", bucket, key)

    try:
        response = glue_client.start_job_run(JobName=GLUE_JOB_NAME)
        job_run_id = response["JobRunId"]
        logger.info(
            "Started Glue job '%s' (JobRunId: %s), triggered by: %s",
            GLUE_JOB_NAME,
            job_run_id,
            triggered_by,
        )
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": f"Started Glue job {GLUE_JOB_NAME}",
                    "jobRunId": job_run_id,
                    "triggeredBy": triggered_by,
                }
            ),
        }

    except glue_client.exceptions.ConcurrentRunsExceededException:
        # The Glue job is already running from a previous trigger — this
        # is expected if several files land close together, so log it
        # as a warning rather than letting Lambda report a failure.
        logger.warning(
            "Glue job '%s' is already running; skipping this trigger.",
            GLUE_JOB_NAME,
        )
        return {
            "statusCode": 200,
            "body": json.dumps(
                {"message": f"{GLUE_JOB_NAME} already running, skipped."}
            ),
        }

    except Exception as e:
        logger.error("Failed to start Glue job '%s': %s", GLUE_JOB_NAME, str(e))
        # Re-raise so Lambda marks this invocation as failed and it shows
        # up clearly in CloudWatch metrics/alarms, instead of silently
        # swallowing a real error.
        raise
