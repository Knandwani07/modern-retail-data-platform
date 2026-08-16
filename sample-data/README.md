# 📊 Sample Data

This folder contains the source datasets used to build and validate the retail analytics platform. These files represent the raw retail data that is ingested into Amazon S3 and processed throughout the AWS and Snowflake data pipeline.

The datasets are used for data ingestion, cataloging, transformation, analytics, and reporting across multiple services including AWS Glue, Amazon Athena, AWS Lake Formation, and Snowflake.

---

## 📁 Dataset Overview

| File | Description |
|--------|-------------|
| **customers.csv** | Customer master data containing customer identifiers and demographic information used for customer-related analytics. |
| **products.json** | Product catalog data stored in JSON format, including nested attributes that demonstrate Snowflake's semi-structured data processing capabilities. |
| **orders.parquet** | Retail transaction data stored in Apache Parquet format containing order details, product references, quantities, pricing, and sales information. |

---

## 🔄 How These Files Are Used

### customers.csv
- Uploaded to the Amazon S3 raw zone.
- Cataloged by AWS Glue Crawlers.
- Used for customer analytics and reporting.

### products.json
- Loaded into Snowflake as semi-structured data.
- Parsed using Snowflake VARIANT columns and JSON functions.
- Used to demonstrate JSON processing and data transformation.

### orders.parquet
- Processed by AWS Glue ETL jobs.
- Stored in the curated data layer.
- Queried using Amazon Athena and Snowflake.
- Used to generate sales and revenue insights.

---

## 🏗️ Role in the Data Pipeline

These datasets serve as the foundation of the end-to-end retail analytics platform:

1. Data is uploaded to Amazon S3.
2. AWS Glue crawls and catalogs the datasets.
3. AWS Glue ETL transforms raw data into curated datasets.
4. Amazon Athena queries curated data.
5. Snowflake loads and analyzes structured and semi-structured data.
6. Business dashboards and visualizations are generated from the processed datasets.

These files are provided solely for educational and demonstration purposes within this project.
