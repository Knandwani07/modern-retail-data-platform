# Create the Parquet File Format

## Purpose

This query creates a Snowflake file format for reading Parquet files stored in Amazon S3.

The file format defines how Snowflake should interpret the incoming data when accessing files through external stages and loading data into tables.

## SQL Query

```sql
CREATE FILE FORMAT retail_pipeline.raw.parquet_fmt
TYPE = PARQUET;
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| File Format Name | `parquet_fmt` | Name of the file format object |
| File Type | `PARQUET` | Columnar file format used for analytics workloads |

## Expected Outcome

- A file format named `PARQUET_FMT` is created in the `RAW` schema.
- Snowflake can interpret Parquet files stored in Amazon S3.
- The file format becomes available for use with external stages and data loading operations.

## Why It Is Used

- Enables Snowflake to read Parquet datasets.
- Provides a reusable configuration for external stages.
- Supports efficient loading of curated data from Amazon S3.
- Improves analytics performance through optimized columnar storage.

## Next Step

Use this file format when creating the external stage that connects Snowflake to the curated data stored in Amazon S3.
