# 🔐 IAM Policies

This folder contains the IAM policies used throughout the Retail Analytics Platform project.

These policies follow the principle of least privilege by granting AWS services only the permissions required to perform specific tasks within the data pipeline.

---

## 📁 Policy Overview

| Policy File | Purpose |
|-------------|---------|
| `glue-retail-s3-access-policy.json` | Grants AWS Glue access to read, write, list, and manage objects within the Amazon S3 data lake. |
| `snowflake-s3-read-policy.json` | Allows Snowflake to securely access curated and raw datasets stored in Amazon S3 through a storage integration. |
| `lambda-start-glue-job-policy.json` | Allows AWS Lambda to trigger AWS Glue ETL jobs automatically when new files arrive in Amazon S3. |

---

## 🎯 Why These Policies Are Required

The retail analytics platform uses multiple AWS services that must interact securely with each other.

These IAM policies enable:

- AWS Glue to read and process raw datasets from Amazon S3.
- AWS Glue to write transformed data into the curated zone.
- Snowflake to access data stored in Amazon S3.
- AWS Lambda to automate ETL job execution.
- Secure communication between AWS services without exposing unnecessary permissions.

---

## 🛡️ Security Considerations

- Always follow the Principle of Least Privilege.
- Restrict permissions to specific buckets, folders, and resources whenever possible.
- Avoid using wildcard (`*`) permissions in production environments.
- Regularly review and audit IAM policies for compliance and security.

These policies form the security foundation of the end-to-end retail analytics pipeline and ensure that each service has the appropriate level of access required to perform its role.
