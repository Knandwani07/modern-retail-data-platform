# Verify Access to the Product Data

## Purpose

This query verifies that Snowflake can successfully access the product dataset stored in Amazon S3 through the configured external stage.

It serves as a validation step before loading JSON data into Snowflake tables.

## SQL Query

```sql
LIST @retail_pipeline.raw.products_stage;
```

## Expected Outcome

- Snowflake successfully connects to the external stage.
- The product JSON file is displayed in the query results.
- File metadata such as file name, size, and last modified timestamp is returned.
- No access or permission errors are generated.

## Validation Checklist

- The `products_stage` external stage exists.
- The `retail_s3_int` storage integration is configured correctly.
- The IAM trust relationship is established successfully.
- The S3 access policy is attached to the IAM role.
- Product files are visible in the stage output.

## Why It Is Used

- Verifies connectivity between Snowflake and Amazon S3.
- Confirms that the storage integration is working correctly.
- Validates access permissions before data loading.
- Ensures the product dataset is available for ingestion.

## Success Criteria

If the product file is listed successfully, the `products_stage` external stage is configured correctly and Snowflake can access the product dataset stored in Amazon S3.
