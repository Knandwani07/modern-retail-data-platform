# 🔗 Snowflake Storage Integration

This folder contains the Snowflake SQL commands used to configure secure access between Snowflake and Amazon S3.

The resources documented here enable Snowflake to read curated retail datasets stored in Amazon S3 through a storage integration, external stages, and file formats. Together, these components establish the connection required for data ingestion and analytics.

---

## 📄 Files

| File | Description |
|--------|-------------|
| `create-storage-integration.md` | Creates the Snowflake storage integration used to securely connect Snowflake to Amazon S3 through an IAM role. |
| `describe-storage-integration.md` | Retrieves storage integration details, including the IAM user ARN and External ID required for AWS trust configuration. |
| `create-parquet-file-format.md` | Creates a Snowflake file format for reading Parquet files stored in Amazon S3. |
| `create-curated-stage.md` | Creates an external stage that points to the curated data location in Amazon S3. |
| `verify-stage-access.md` | Validates that Snowflake can successfully access files stored in the configured S3 stage. |

---

## 🎯 Purpose

The files in this folder are used to:

- Establish secure connectivity between Snowflake and Amazon S3.
- Configure storage integrations using AWS IAM roles.
- Define file formats for reading Parquet datasets.
- Create external stages for accessing curated retail data.
- Validate connectivity before loading or querying data.

---

## 🔄 Configuration Workflow

1. Create the Snowflake storage integration.
2. Retrieve the generated IAM User ARN and External ID.
3. Configure the AWS trust relationship.
4. Create the Parquet file format.
5. Create the external stage pointing to the curated S3 location.
6. Verify that Snowflake can access the staged files.

---

## 🔧 Components Covered

- Snowflake Storage Integration
- Amazon S3
- AWS IAM Roles
- External Stages
- Parquet File Formats

---

## 📌 Notes

- Replace placeholder values such as bucket names, IAM role ARNs, and AWS account details before execution.
- The storage integration must be configured successfully before creating external stages.
- Stage access should be validated before loading data into Snowflake tables.
