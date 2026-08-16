# Create the Curated Orders Table

## Purpose

This query creates the `orders_curated` table in Snowflake.

The table is designed to store cleansed and analytics-ready order data loaded from the curated layer of the Amazon S3 data lake. Unlike the raw product dataset, this table uses a structured schema with predefined columns and data types.

## SQL Query

```sql
CREATE TABLE retail_pipeline.raw.orders_curated (
    order_id STRING,
    customer_id STRING,
    product_id STRING,
    order_date DATE,
    quantity INT,
    unit_price NUMBER(10,2),
    order_total NUMBER(10,2)
);
```

## Column Definitions

| Column | Data Type | Description |
|----------|----------|-------------|
| `order_id` | STRING | Unique identifier for each order |
| `customer_id` | STRING | Unique customer identifier |
| `product_id` | STRING | Unique product identifier |
| `order_date` | DATE | Date the order was placed |
| `quantity` | INT | Number of units ordered |
| `unit_price` | NUMBER(10,2) | Price per unit |
| `order_total` | NUMBER(10,2) | Total order value |

## Expected Outcome

- A table named `ORDERS_CURATED` is created in the `RAW` schema.
- The table structure is ready to receive curated order data.
- All required columns and data types are defined for analytics workloads.

## Why It Is Used

- Stores cleansed and curated order data.
- Provides a structured schema for reporting and analytics.
- Supports business intelligence workloads in Snowflake.
- Serves as the primary fact table for retail sales analysis.

## Next Step

Load the curated Parquet dataset from the external stage into the `orders_curated` table using the `COPY INTO` command.
