# Load Product JSON Data into Snowflake

## Purpose

This query loads the product JSON dataset from the external stage into the `products_raw` table.

The JSON records are stored in the `raw_data` VARIANT column, allowing Snowflake to preserve the original semi-structured data for further transformation and analysis.

## SQL Query

```sql
COPY INTO retail_pipeline.raw.products_raw
FROM @retail_pipeline.raw.products_stage
FILE_FORMAT = (FORMAT_NAME = retail_pipeline.raw.json_fmt);
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Target Table | `products_raw` | Stores raw product JSON data |
| Source Stage | `products_stage` | External stage pointing to the S3 product dataset |
| File Format | `json_fmt` | JSON file format definition |
| Command | `COPY INTO` | Loads data from S3 into Snowflake |

## Expected Outcome

- Product JSON records are loaded into the `products_raw` table.
- Each JSON document is stored in the `raw_data` VARIANT column.
- Snowflake returns the load status and number of rows loaded.
- No loading or parsing errors are generated.

## Why It Is Used

- Ingests product data from Amazon S3 into Snowflake.
- Preserves the original JSON structure.
- Supports downstream transformations and analytics.
- Creates the foundation for converting semi-structured data into relational tables.
