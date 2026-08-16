# Create the Products External Stage

## Purpose

This query creates an external stage that connects Snowflake to the product JSON files stored in Amazon S3.

The stage uses the configured storage integration and JSON file format to provide secure access to product data stored in the data lake.

## SQL Query

```sql
CREATE STAGE retail_pipeline.raw.products_stage
  URL = 's3://<your-s3-bucket-name>/raw/products/'
  STORAGE_INTEGRATION = retail_s3_int
  FILE_FORMAT = retail_pipeline.raw.json_fmt;
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Stage Name | `products_stage` | External stage used for product data |
| S3 Location | `raw/products/` | Location of the product JSON dataset |
| Storage Integration | `retail_s3_int` | Secure connection between Snowflake and Amazon S3 |
| File Format | `json_fmt` | Defines JSON as the source file format |

> Replace `<your-s3-bucket-name>` with your Amazon S3 bucket name before executing the query.

## Expected Outcome

- A new external stage named `PRODUCTS_STAGE` is created.
- Snowflake can securely access files stored in the `raw/products/` S3 location.
- The stage is available for file validation and data loading operations.

## Why It Is Used

- Connects Snowflake to the product dataset stored in Amazon S3.
- Enables secure access through a Storage Integration.
- Provides a reusable location for loading JSON files.
- Supports ingestion of semi-structured product data into Snowflake.

## Next Step

Validate the stage configuration by listing the files available in the stage using the `LIST` command.
