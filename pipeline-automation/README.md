# ⚡ AWS Lambda Automation

This folder contains the AWS Lambda function used to automate the retail analytics pipeline.

The function is triggered whenever a new file is uploaded to the `raw/orders/` location in Amazon S3. Upon receiving the event, the Lambda function automatically starts the AWS Glue ETL job, eliminating the need for manual execution and enabling an event-driven data processing workflow. :contentReference[oaicite:0]{index=0}

---

## 📄 Files

| File | Description |
|--------|-------------|
| `trigger-retail-pipeline.py` | Lambda function that listens for S3 object creation events and starts the AWS Glue ETL job automatically. |

---

## 🔄 Workflow

1. A new file is uploaded to the Amazon S3 `raw/orders/` folder.
2. Amazon S3 triggers the Lambda function.
3. The Lambda function identifies the uploaded object and logs the event.
4. AWS Glue job `retail-transform-orders` is started automatically.
5. The ETL process transforms raw data and writes curated output to Amazon S3. :contentReference[oaicite:1]{index=1}

---

## 🎯 Business Value

- Automates ETL job execution.
- Eliminates manual intervention.
- Enables event-driven data processing.
- Reduces operational overhead.
- Improves data pipeline efficiency and scalability.

---

## 🔧 AWS Services Used

- AWS Lambda
- Amazon S3
- AWS Glue
- Amazon CloudWatch Logs
- AWS IAM
