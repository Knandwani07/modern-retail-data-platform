# Verify Access to the Curated Stage

## Purpose

This query validates that Snowflake can successfully access the curated data stored in Amazon S3 through the configured storage integration and external stage.

It is commonly used as a connectivity test before loading data into Snowflake tables.

## SQL Query

```sql
LIST @retail_pipeline.raw.curated_stage;
```

## Expected Outcome

- Snowflake successfully connects to the S3 bucket.
- Files stored in the `curated/` folder are displayed.
- File names, sizes, and last modified timestamps are returned.
- No access or permission errors are generated.

## Sample Output

| Name | Size | Last Modified |
|--------|--------|--------|
| orders_curated.parquet | 12 KB | 2026-08-15 |
| part-00000.parquet | 8 KB | 2026-08-15 |

## Why It Is Used

- Verifies the storage integration is configured correctly.
- Confirms the IAM role trust relationship is working.
- Validates S3 permissions before loading data.
- Ensures Snowflake can access curated datasets stored in Amazon S3.

## Validation Checklist

- External stage exists.
- Storage integration is active.
- IAM trust policy is configured correctly.
- S3 read permissions are attached.
- Curated files are visible in the stage output.

## Next Step

Once the stage contents are visible, the curated dataset can be loaded into Snowflake tables using the `COPY INTO` command.
