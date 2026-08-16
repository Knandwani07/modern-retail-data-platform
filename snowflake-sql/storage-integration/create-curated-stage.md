# Create the Curated Data Stage

## Purpose

This query creates an external Snowflake stage that connects to the curated data stored in Amazon S3.

The stage uses the previously created storage integration and Parquet file format, allowing Snowflake to securely access the curated dataset.

## SQL Query

```sql
CREATE FILE FORMAT retail_pipeline.raw.parquet_fmt
TYPE = PARQUET;

CREATE STAGE retail_pipeline.raw.curated_stage
  URL = 's3://<your-s3-bucket-name>/curated/'
  STORAGE_INTEGRATION = retail_s3_int
  FILE_FORMAT = retail_pipeline.raw.parquet_fmt;
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| File Format | `parquet_fmt` | Defines Parquet as the source file format |
| Stage | `curated_stage` | External stage for the curated S3 data |
| S3 Location | `curated/` | Location containing the transformed datasets |
| Storage Integration | `retail_s3_int` | Provides secure access between Snowflake and S3 |

Replace `<your-s3-bucket-name>` with the name of your S3 bucket before executing the query.

## Expected Outcome

- The `PARQUET_FMT` file format is created.
- The `CURATED_STAGE` external stage is created successfully.
- Snowflake can access the curated S3 location through the configured storage integration.

## Why It Is Used

- Connects Snowflake to the curated S3 data.
- Enables secure access without storing AWS credentials in Snowflake.
- Provides a reusable stage for loading curated Parquet data.
- Forms the connection between the AWS data lake and Snowflake analytics layer.
