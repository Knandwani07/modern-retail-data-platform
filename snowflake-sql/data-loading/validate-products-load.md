# Validate Product Data Load

## Purpose

This query verifies that the product dataset was loaded successfully into the `products_raw` table.

It returns the total number of records currently stored in the table and helps confirm that the Snowflake data load completed successfully.

## SQL Query

```sql
SELECT COUNT(*) AS total_records
FROM retail_pipeline.raw.products_raw;
```

## Expected Outcome

- Snowflake returns the total number of records loaded into the table.
- The record count matches the number of JSON records in the source dataset.
- No query execution errors are generated.

## Sample Output

| TOTAL_RECORDS |
|--------------:|
| 100 |

## Why It Is Used

- Validates successful data ingestion.
- Confirms that records were loaded into Snowflake.
- Helps identify incomplete or failed loads.
- Provides a quick data quality check before transformations.

## Validation Checklist

- The `products_raw` table exists.
- The `COPY INTO` operation completed successfully.
- The returned row count is greater than zero.
- The record count matches the source dataset.

## Next Step

Once the record count is verified, the raw JSON data can be transformed into a structured table for analytics and reporting.
