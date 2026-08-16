# Flatten Product Tags from JSON Data

## Purpose

This query extracts product attributes from the raw JSON dataset and flattens the nested `tags` array into individual rows.

The transformation converts semi-structured JSON data into a relational format that is easier to query, analyze, and report on.

## SQL Query

```sql
SELECT
  data:product_id::string AS product_id,
  data:name::string AS product_name,
  data:category::string AS category,
  f.value::string AS tag
FROM retail_pipeline.raw.products_raw,
     LATERAL FLATTEN(input => data:tags) f;
```

## Configuration Details

| Component | Description |
|------------|-------------|
| `product_id` | Extracts the product identifier from the JSON document |
| `product_name` | Extracts the product name |
| `category` | Extracts the product category |
| `FLATTEN()` | Expands the tags array into individual rows |
| `tag` | Returns each tag as a separate value |

## Expected Outcome

- Product information is extracted from the JSON records.
- Each tag is returned as a separate row.
- Nested JSON arrays are converted into a tabular structure.
- The dataset becomes easier to analyze using SQL.

## Why It Is Used

- Transforms semi-structured JSON into relational data.
- Enables analysis of individual product tags.
- Simplifies reporting and aggregation.
- Demonstrates Snowflake's support for semi-structured data processing.

## Example Output

| product_id | product_name | category | tag |
|------------|-------------|----------|-----|
| P101 | Wireless Mouse | Electronics | wireless |
| P101 | Wireless Mouse | Electronics | office |
| P101 | Wireless Mouse | Electronics | computer |

## Next Step

Use the transformed output to create structured analytics tables or run category and product-based reporting queries.
