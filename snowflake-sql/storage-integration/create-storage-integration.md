# Create the Snowflake Storage Integration

## Purpose

This query creates a Snowflake Storage Integration that enables secure access between Snowflake and Amazon S3.

The integration allows Snowflake to read data stored in the S3 data lake without requiring AWS access keys, using an IAM role instead.

## SQL Query

```sql
CREATE STORAGE INTEGRATION retail_s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = 'S3'
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::<your-account-id>:role/SnowflakeS3AccessRole'
STORAGE_ALLOWED_LOCATIONS = (
    's3://<your-bucket-name>/curated/'
);
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Integration Name | `retail_s3_int` | Name of the Snowflake storage integration |
| Storage Provider | `S3` | Amazon S3 storage service |
| Enabled | `TRUE` | Activates the integration |
| IAM Role | `SnowflakeS3AccessRole` | AWS IAM role assumed by Snowflake |
| Allowed Location | `curated/` | Restricts access to the curated data layer |

## Expected Outcome

- A storage integration named `RETAIL_S3_INT` is created.
- Snowflake can securely assume the specified IAM role.
- Access is limited to the configured S3 location.
- The integration becomes available for use with external stages.

## Why It Is Used

- Enables secure Snowflake-to-S3 connectivity.
- Eliminates the need for AWS access keys.
- Restricts access to approved S3 locations.
- Provides the foundation for loading curated data into Snowflake.
