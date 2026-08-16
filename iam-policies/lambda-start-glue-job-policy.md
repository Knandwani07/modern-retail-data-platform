# 🚀 Lambda Start Glue Job Policy

## 📖 Overview

This policy grants the AWS Lambda function permission to start an AWS Glue ETL job.

Within this project, the `trigger-retail-pipeline` Lambda function is automatically invoked whenever a new file is uploaded to the Amazon S3 `raw/orders/` folder. The function uses this permission to start the `retail-transform-orders` AWS Glue job, enabling automated and event-driven data processing.

---

## 🎯 Purpose

This policy is required to:

- Allow AWS Lambda to invoke AWS Glue jobs.
- Automate ETL execution when new data arrives.
- Eliminate manual job execution.
- Enable event-driven orchestration of the retail analytics pipeline.

---

## 🔗 Attached To

```text
Lambda Execution Role
```

---

## ⚙️ Used By

```text
trigger-retail-pipeline
```

---

## 🔐 Permissions Granted

| Permission | Description |
|------------|-------------|
| `glue:StartJobRun` | Allows the Lambda function to start an AWS Glue ETL job programmatically. |

---

## 📄 Policy Document

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:StartJobRun"
      ],
      "Resource": "*"
    }
  ]
}
```

---

## 🔄 Workflow

1. A new file is uploaded to the Amazon S3 `raw/orders/` folder.
2. Amazon S3 generates an Object Created event.
3. The `trigger-retail-pipeline` Lambda function is invoked.
4. Lambda uses the `glue:StartJobRun` permission to start the `retail-transform-orders` AWS Glue job.
5. AWS Glue processes the incoming data and writes the transformed output to the curated data layer.

---

## 💡 Why This Policy Is Important

Without this policy, the Lambda function would not have permission to start AWS Glue jobs. As a result, newly uploaded data would require manual processing.

By granting the `glue:StartJobRun` permission, the pipeline becomes fully automated, ensuring that data is transformed and made available for analytics immediately after arrival.

---

## 🏗️ Services Involved

- Amazon S3
- AWS Lambda
- AWS Glue
- Amazon CloudWatch
- AWS IAM
