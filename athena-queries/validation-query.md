# Dataset Validation Query

## Purpose

This query validates the curated dataset by comparing the total number of records with the number of unique order IDs.

It helps confirm that:

- Data was loaded successfully into the curated layer.
- No duplicate order records exist.
- The ETL transformation completed correctly.
- The dataset is ready for analytics and reporting.

## Query

```sql
SELECT COUNT(*) AS total_rows,
       COUNT(DISTINCT order_id) AS distinct_orders
FROM curated;
```

## Expected Output

| Column | Description |
|----------|-------------|
| total_rows | Total number of records in the curated dataset |
| distinct_orders | Number of unique order IDs |

## Validation Criteria

The values of `total_rows` and `distinct_orders` should match.

Example:

| total_rows | distinct_orders |
|------------|------------------|
| 193 | 193 |

Matching values indicate that:

- Every order record is unique.
- No duplicate orders were introduced during processing.
- The curated dataset is ready for downstream analytics.

## Business Value

This validation query serves as a data quality check before performing reporting, dashboarding, and business analysis.
