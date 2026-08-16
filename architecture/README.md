# 🏗️ Architecture

This folder contains the architecture documentation for the Modern Retail Data Platform on AWS and Snowflake.

The architecture combines automated data processing on AWS with manual batch analytics in Snowflake. Raw retail data is ingested into Amazon S3, transformed using AWS Glue, cataloged for querying with Amazon Athena, and selectively loaded into Snowflake for additional analytics.

---

## 📄 Files

| File | Description |
|--------|-------------|
| `architecture-overview.md` | End-to-end explanation of how data moves through the platform. |
| `architecture-components.md` | Detailed description of each AWS and Snowflake component used in the solution. |

---

## 🎯 Architecture Goals

- Centralize retail data in Amazon S3.
- Automate data ingestion and transformation.
- Maintain a curated analytics dataset.
- Enable SQL-based analytics through Athena.
- Load curated datasets into Snowflake for additional reporting.
- Demonstrate a modern cloud-native data platform architecture.

---

## 🔄 High-Level Data Flow

1. Raw data is uploaded to Amazon S3.
2. AWS Glue Crawlers discover and catalog datasets.
3. AWS Glue ETL transforms raw files into curated Parquet datasets.
4. AWS Glue Data Catalog stores metadata.
5. Amazon Athena queries curated datasets.
6. Snowflake accesses curated and product datasets through external stages.
7. Data is loaded into Snowflake tables for analysis.

---

## 🔧 Technologies Used

- Amazon S3
- AWS Glue
- AWS Lambda
- AWS Lake Formation
- AWS IAM
- Amazon Athena
- Snowflake
- Snowflake Storage Integration
- Snowflake External Stages
