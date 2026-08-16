import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)
GLUE_JOB_NAME = "retail-transform-orders"
glue_client = boto3.client("glue")

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event))
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
        raise
