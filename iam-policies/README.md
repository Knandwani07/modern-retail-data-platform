# 🔐 IAM Policies

This folder contains the IAM policies used throughout the Modern Retail Data Platform project.

These policies provide the permissions required for AWS Glue, AWS Lambda, Amazon S3, and Snowflake integrations to securely access and process data across the platform.

---

## 📁 Policy Overview

| File | Purpose |
|--------|---------|
| `glue-retail-s3-access-policy.md` | Grants AWS Glue permission to read, write, list, and delete objects within the retail data lake S3 bucket. |
| `lambda-start-glue-job-policy.md` | Allows the Lambda function to trigger AWS Glue jobs using the `glue:StartJobRun` action. |
| `snowflake-trust-policy.md` | Establishes the trust relationship between Snowflake and AWS IAM, allowing Snowflake to assume the configured IAM role. |
| `snowflake-s3-read-policy.md` | Grants Snowflake read access to curated data stored in Amazon S3. |
| `snowflake-s3-read-policy-update.md` | Extends Snowflake permissions to access both curated datasets and raw product files stored in Amazon S3. |

---

## 🎯 Why These Policies Are Required

These IAM policies enable secure communication between services while following AWS access control best practices.

They are used to:

- Allow AWS Glue to process data stored in Amazon S3.
- Allow AWS Lambda to automate Glue job execution.
- Enable Snowflake to securely connect to AWS resources.
- Control access to curated and raw datasets.
- Support secure data ingestion and analytics workflows.

---

## 🔄 Services Covered

The policies in this folder support the following services:

- AWS Identity and Access Management (IAM)
- Amazon S3
- AWS Glue
- AWS Lambda
- Snowflake Storage Integrations

---

## 📌 Notes

- Update bucket names, ARNs, account IDs, and external IDs before deploying in your own AWS environment.
- Review permissions carefully before applying them in production environments.
- Follow the deployment guide to understand where each policy is used within the project workflow.
