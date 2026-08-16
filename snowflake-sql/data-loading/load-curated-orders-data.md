# Load Curated Orders Data into Snowflake

## Purpose

This query loads the curated orders dataset from the Snowflake external stage into the `orders_curated` table.

The `MATCH_BY_COLUMN_NAME` option automatically maps source columns to target table columns, making the data loading process more flexible and reducing dependency on column order.

## SQL Query

```sql
COPY INTO retail_pipeline.raw.orders_curated
FROM @retail_pipeline.raw.curated_stage
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE;
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Target Table | `orders_curated` | Destination table for curated order data |
| Source Stage | `curated_stage` | External stage pointing to the curated S3 dataset |
| Load Method | `COPY INTO` | Snowflake bulk data loading command |
| Column Mapping | `CASE_INSENSITIVE` | Matches source and target columns regardless of letter case |

## Expected Outcome

- Curated order records are loaded into the `orders_curated` table.
- Source columns are mapped automatically to matching table columns.
- Snowflake returns the load status and row count.
- The dataset becomes available for analytics and reporting.

## Why It Is Used

- Loads curated data from Amazon S3 into Snowflake.
- Simplifies ingestion through automatic column mapping.
- Supports scalable and efficient bulk loading.
- Prepares the dataset for business intelligence and analytical workloads.

## Next Step

Run validation queries to confirm that all records were loaded successfully and that the row counts match the source data in AWS Glue and Amazon Athena.
