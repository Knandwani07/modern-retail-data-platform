# 🧹 Cleanup Guide

This guide explains how to remove all AWS and Snowflake resources created during the project to prevent unnecessary charges.

> **Important:** Complete the cleanup steps only after you have finished testing, validation, and analytics activities.

---

## AWS Resource Cleanup

Delete AWS resources in the order shown below to avoid dependency conflicts.

### 1. Delete the Lambda Function

Navigate to:

```text
AWS Lambda → Functions
```

Delete:

```text
trigger-retail-pipeline
```

Purpose:

- Stops automated pipeline execution.
- Prevents accidental Glue job triggers.

---

### 2. Delete AWS Glue Resources

Navigate to:

```text
AWS Glue
```

Delete:

- Glue Job
- Glue Crawler
- Glue Database

Purpose:

- Removes ETL resources.
- Prevents future Glue charges.

---

### 3. Delete Amazon Athena Resources

Navigate to:

```text
Amazon Athena
```

Delete:

- Athena Tables
- Athena Database

Purpose:

- Removes query metadata and catalog objects.

---

### 4. Empty the S3 Bucket

Navigate to:

```text
Amazon S3
```

Delete all objects from:

```text
raw/
curated/
athena-results/
```

Purpose:

- Removes stored datasets and query results.
- Eliminates S3 storage costs.

---

### 5. Delete the S3 Bucket

After the bucket is empty, delete:

```text
retail-analytics-data-lake-pipeline-2026
```

Purpose:

- Removes the data lake infrastructure.

---

### 6. Delete IAM Roles and Policies

Navigate to:

```text
IAM → Roles
```

Delete:

```text
GlueRetailPipelineRole
SnowflakeS3AccessRole
```

Remove associated inline policies:

```text
RetailPipelineS3Access
SnowflakeS3ReadPolicy
```

Purpose:

- Removes unused access permissions.
- Follows security best practices.

---

## Snowflake Resource Cleanup

### 7. Drop External Stages

```sql
DROP STAGE IF EXISTS retail_pipeline.raw.curated_stage;

DROP STAGE IF EXISTS retail_pipeline.raw.products_stage;
```

Purpose:

- Removes S3 connections from Snowflake.

---

### 8. Drop File Formats

```sql
DROP FILE FORMAT IF EXISTS retail_pipeline.raw.parquet_fmt;

DROP FILE FORMAT IF EXISTS retail_pipeline.raw.json_fmt;
```

Purpose:

- Removes reusable file format objects.

---

### 9. Drop Storage Integration

```sql
DROP INTEGRATION IF EXISTS retail_s3_int;
```

Purpose:

- Removes the Snowflake-to-S3 connection.

---

### 10. Drop Tables

```sql
DROP TABLE IF EXISTS retail_pipeline.raw.orders_curated;

DROP TABLE IF EXISTS retail_pipeline.raw.products_raw;
```

Purpose:

- Removes loaded datasets.

---

### 11. Drop the Schema

```sql
DROP SCHEMA IF EXISTS retail_pipeline.raw;
```

Purpose:

- Removes schema-level objects.

---

### 12. Drop the Database

```sql
DROP DATABASE IF EXISTS retail_pipeline;
```

Purpose:

- Removes the entire project database.

---

### 13. Drop the Warehouse

```sql
DROP WAREHOUSE IF EXISTS retail_wh;
```

Purpose:

- Stops Snowflake compute charges.

---

## Cleanup Validation Checklist

### AWS

- Lambda function deleted
- Glue job deleted
- Glue crawler deleted
- Glue database deleted
- Athena database deleted
- Athena tables deleted
- S3 bucket emptied
- S3 bucket deleted
- IAM roles deleted
- IAM policies deleted

### Snowflake

- External stages dropped
- File formats dropped
- Storage integration dropped
- Tables dropped
- Schema dropped
- Database dropped
- Warehouse dropped

---

## Expected Result

After completing the cleanup process:

- No AWS resources remain deployed.
- No Snowflake resources remain active.
- No storage or compute charges continue to accrue.
- The environment is fully removed and ready for a future redeployment.
