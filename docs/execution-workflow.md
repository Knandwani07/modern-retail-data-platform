# 🔄 Execution Workflow

This document describes how data flows through the platform after all resources have been deployed.

---

## End-to-End Workflow

```text
Raw Data
    │
    ▼
Amazon S3
    │
    ▼
AWS Lambda
    │
    ▼
AWS Glue ETL
    │
    ▼
Curated Parquet Data
    │
    ├────► Amazon Athena
    │
    ▼
Snowflake
    │
    ▼
Analytics & Reporting
```

---

## Step 1 — Data Ingestion

Source files are uploaded to:

```text
raw/customers/
raw/orders/
raw/products/
```

These files become the input for the pipeline.

---

## Step 2 — Pipeline Trigger

The Lambda function is invoked.

Function:

```text
trigger-retail-pipeline
```

Lambda starts the AWS Glue ETL job.

---

## Step 3 — Data Transformation

AWS Glue:

- Reads raw order data
- Cleans records
- Applies transformations
- Converts output to Parquet

Output:

```text
curated/
```

---

## Step 4 — Curated Data Storage

The transformed dataset is written back to Amazon S3.

Benefits:

- Optimized storage
- Faster queries
- Analytics-ready format

---

## Step 5 — Data Validation with Athena

Athena queries the curated dataset.

Validation includes:

- Row counts
- Data quality checks
- Query testing

---

## Step 6 — Snowflake Access

Snowflake connects to Amazon S3 through:

```text
Storage Integration
```

The external stages expose the curated and product datasets.

---

## Step 7 — Product Data Processing

Snowflake:

- Reads product JSON files
- Loads records into products_raw
- Stores semi-structured data using VARIANT

---

## Step 8 — Orders Data Processing

Snowflake:

- Reads curated Parquet files
- Loads records into orders_curated
- Creates structured analytics tables

---

## Step 9 — Analytics Layer

Business queries are executed to generate insights such as:

- Revenue by Category
- Revenue by City
- Top Selling Products
- Customer Metrics

---

## Step 10 — Visualization

Query results are transformed into charts and dashboards for business reporting.

---

## Final Outcome

The platform converts raw retail datasets into analytics-ready data using AWS for data engineering and Snowflake for cloud data warehousing and reporting.
