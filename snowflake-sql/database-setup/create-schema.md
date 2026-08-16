# Create the Raw Data Schema

## Purpose

This query creates the `RAW` schema inside the `RETAIL_PIPELINE` database.

The schema is used to store raw and staging data loaded into Snowflake before it is transformed and analyzed.

## SQL Query

```sql
CREATE SCHEMA retail_pipeline.raw;
```

## Expected Outcome

- A new schema named `RAW` is created within the `RETAIL_PIPELINE` database.
- The schema becomes visible in Snowsight under the database.
- Tables, stages, and file formats can be created within this schema.

## Why It Is Used

- Organizes raw data assets in a dedicated location.
- Separates ingestion and staging objects from analytics workloads.
- Provides a structured environment for loading and transforming data.
