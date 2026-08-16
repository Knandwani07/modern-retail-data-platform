# ⚡ AWS Lambda Automation

This folder contains the AWS Lambda resources used to automate the retail analytics pipeline.

The Lambda function is triggered whenever a new file is uploaded to the `raw/orders/` location in Amazon S3. Once triggered, the function automatically starts the AWS Glue ETL job, enabling a fully event-driven data processing workflow without manual intervention.

---

## 📄 Files

| File | Description |
|--------|-------------|
| `trigger-retail-pipeline.py` | Lambda function that listens for S3 object creation events and automatically starts the AWS Glue ETL job. |
| `sample-s3-event.json` | Sample Amazon S3 event payload used for testing and validating the Lambda trigger configuration. |

---

## 🔄 Workflow

1. A new order file is uploaded to the Amazon S3 `raw/orders/` folder.
2. Amazon S3 generates an `ObjectCreated` event.
3. The event triggers the Lambda function.
4. The Lambda function reads the event details and identifies the uploaded file.
5. The Lambda function starts the `retail-transform-orders` AWS Glue job.
6. AWS Glue processes the raw data and writes curated output to Amazon S3.
7. Logs and execution details are recorded in Amazon CloudWatch.

---

## 🎯 Business Value

- Automates data ingestion and transformation workflows.
- Eliminates manual Glue job execution.
- Enables near real-time processing of incoming datasets.
- Reduces operational overhead and human error.
- Improves scalability and reliability of the data platform.

---

## 🔧 AWS Services Used

- AWS Lambda
- Amazon S3
- AWS Glue
- Amazon CloudWatch Logs
- AWS Identity and Access Management (IAM)

---

## 📌 Notes

- The Lambda function requires IAM permissions to start AWS Glue jobs.
- Amazon S3 event notifications must be configured on the `raw/orders/` prefix.
- The sample event file can be used to test the function directly from the AWS Lambda console before enabling production triggers.
