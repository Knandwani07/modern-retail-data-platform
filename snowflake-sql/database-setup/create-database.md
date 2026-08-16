# Create the Project Database

## Purpose

This query creates the primary Snowflake database used throughout the Retail Analytics Platform project.

The database serves as the top-level container for all project resources, including schemas, tables, stages, file formats, and analytics objects.

## SQL Query

```sql
CREATE DATABASE retail_pipeline;
```

## Expected Outcome

- A new database named `RETAIL_PIPELINE` is created.
- The database becomes visible in Snowsight.
- Project resources can now be created within the database.

## Why It Is Used

- Organizes all project data in a single location.
- Provides logical separation from other Snowflake workloads.
- Forms the foundation for the retail analytics environment.
