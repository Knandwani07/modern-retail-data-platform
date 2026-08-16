# Load Product Data into the Raw Table

## Purpose

This query loads the product JSON dataset from the external stage into the `products_raw` table.

The data is ingested directly from Amazon S3 and stored in the `VARIANT` column, preserving the original JSON structure for downstream transformations.

## SQL Query

```sql
COPY INTO retail_pipeline.raw.products_raw
FROM @retail_pipeline.raw.products_stage
FILE_FORMAT = (FORMAT_NAME = retail_pipeline.raw.json_fmt);
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Target Table | `products_raw` | Destination table for raw product data |
| Source Stage | `products_stage` | External stage containing the product JSON file |
| File Format | `json_fmt` | JSON file format definition |
| Command | `COPY INTO` | Snowflake bulk data loading command |

## Expected Outcome

- Product records are loaded into the `products_raw` table.
- JSON documents are stored in the `raw_data` VARIANT column.
- Snowflake returns the load status and row count.
- No loading or parsing errors are generated.

## Why It Is Used

- Loads product data from Amazon S3 into Snowflake.
- Preserves the original JSON structure.
- Supports semi-structured data processing.
- Provides the source dataset for future transformations and analytics.

## Next Step

Validate the load by querying the `products_raw` table and confirming that the expected number of records has been imported successfully.
