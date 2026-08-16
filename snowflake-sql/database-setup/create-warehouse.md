# Create the Compute Warehouse

## Purpose

This query creates a Snowflake virtual warehouse named `RETAIL_WH`.

A warehouse provides the compute resources required to execute SQL queries, load data, perform transformations, and run analytics within Snowflake.

## SQL Query

```sql
CREATE WAREHOUSE retail_wh
WITH
    WAREHOUSE_SIZE = 'XSMALL'
    AUTO_SUSPEND = 60
    AUTO_RESUME = TRUE;
```

## Configuration Details

| Setting | Value | Description |
|----------|---------|-------------|
| Warehouse Name | `retail_wh` | Name of the virtual warehouse |
| Warehouse Size | `XSMALL` | Small compute size suitable for development and testing |
| Auto Suspend | `60` seconds | Automatically stops the warehouse after 60 seconds of inactivity |
| Auto Resume | `TRUE` | Automatically starts the warehouse when a query is executed |

## Expected Outcome

- A new warehouse named `RETAIL_WH` is created.
- The warehouse becomes visible in Snowsight.
- Compute resources are available for data loading, transformations, and analytics.

## Why It Is Used

- Provides compute resources for Snowflake workloads.
- Processes SQL queries and data transformations.
- Automatically reduces costs through auto-suspend.
- Resumes automatically when new workloads arrive.
