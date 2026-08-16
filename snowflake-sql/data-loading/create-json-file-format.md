# Create the JSON File Format

## Purpose

This query creates a Snowflake file format for reading JSON files stored in Amazon S3.

The file format enables Snowflake to correctly interpret semi-structured JSON data and prepares it for loading into Snowflake tables.

## SQL Query

```sql
CREATE FILE FORMAT retail_pipeline.raw.json_fmt
TYPE = JSON;
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| File Format Name | `json_fmt` | Name of the file format object |
| File Type | `JSON` | Semi-structured data format |

## Expected Outcome

- A file format named `JSON_FMT` is created in the `RAW` schema.
- Snowflake can interpret JSON files stored in Amazon S3.
- The file format becomes available for use with external stages and data loading operations.

## Why It Is Used

- Enables Snowflake to read JSON datasets.
- Supports ingestion of semi-structured data.
- Provides a reusable configuration for external stages.
- Allows JSON data to be loaded into Snowflake tables for further transformation and analysis.

## Next Step

Use this file format when creating the external stage for the product dataset stored in the `raw/products/` S3 location.
