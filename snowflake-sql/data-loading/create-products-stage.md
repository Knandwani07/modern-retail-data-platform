# Create the Products Data Stage

## Purpose

This query creates an external Snowflake stage that connects to the product JSON files stored in Amazon S3.

The stage uses the Snowflake storage integration and JSON file format, allowing Snowflake to securely access and load product data from the data lake.

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
| Stage Name | `products_stage` | External stage for product data |
| S3 Location | `raw/products/` | Location containing product JSON files |
| Storage Integration | `retail_s3_int` | Secure connection between Snowflake and Amazon S3 |
| File Format | `json_fmt` | Defines JSON as the source file format |

Replace `<your-s3-bucket-name>` with the name of your Amazon S3 bucket before executing the query.

## Expected Outcome

- A new external stage named `PRODUCTS_STAGE` is created.
- Snowflake can access files stored in the `raw/products/` location.
- The stage becomes available for data loading operations.

## Why It Is Used

- Connects Snowflake to product data stored in Amazon S3.
- Enables secure access through the storage integration.
- Provides a reusable location for loading JSON datasets.
- Supports ingestion of semi-structured product data into Snowflake.

## Next Step

Validate the stage by listing its contents and confirming that the product JSON files are accessible from Snowflake.
