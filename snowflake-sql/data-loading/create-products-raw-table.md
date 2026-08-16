# Create the Raw Products Table

## Purpose

This query creates a Snowflake table for storing the raw product data loaded from the JSON dataset.

The table uses the `VARIANT` data type, which is designed to store semi-structured data such as JSON. This allows Snowflake to ingest the raw dataset before transforming it into an analytics-ready format.

## SQL Query

```sql
CREATE OR REPLACE TABLE retail_pipeline.raw.products_raw (
    raw_data VARIANT
);
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Table Name | `products_raw` | Stores raw product data |
| Column Name | `raw_data` | Holds the complete JSON record |
| Data Type | `VARIANT` | Snowflake data type for semi-structured data |

## Expected Outcome

- A table named `PRODUCTS_RAW` is created in the `RAW` schema.
- The table is ready to receive JSON records from Amazon S3.
- Each JSON document is stored as a single record in the `raw_data` column.

## Why It Is Used

- Stores raw product data before transformation.
- Supports ingestion of semi-structured JSON datasets.
- Enables flexible querying of nested JSON attributes.
- Serves as the source table for downstream transformations and analytics.

## Next Step

Load the product JSON dataset from the external stage into the `products_raw` table using the `COPY INTO` command.
