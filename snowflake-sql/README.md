# ❄️ Snowflake SQL Scripts

This folder contains the SQL scripts used to build, configure, and analyze data within Snowflake for the Retail Analytics Platform.

The scripts cover the complete Snowflake workflow, including environment setup, Amazon S3 integration, data loading, JSON transformation, validation, and analytics.

---

## 📂 Folder Structure

```text
snowflake-sql/
├── database-setup/
├── storage-integration/
├── data-loading/
├── transformations/
├── analytics/
└── README.md
```

### database-setup/

Contains scripts for creating:

- Databases
- Schemas
- Warehouses

### storage-integration/

Contains scripts for:

- Storage Integrations
- External Stages
- File Formats
- Amazon S3 connectivity

### data-loading/

Contains scripts used to:

- Load curated Parquet data
- Load JSON datasets
- Populate Snowflake tables

### transformations/

Contains SQL transformations for:

- Parsing semi-structured JSON data
- Flattening nested arrays
- Creating analytics-ready datasets

### analytics/

Contains business intelligence and reporting queries used to generate insights from the retail dataset.

---

## 🎯 Purpose

These scripts demonstrate how Snowflake can be integrated with an AWS-based data lake to create a modern analytics platform.

The queries support:

- Data ingestion
- Data transformation
- Data validation
- Data warehousing
- Business analytics

---

## 🔧 Technologies Used

- Snowflake
- Amazon S3
- SQL
- Semi-Structured Data (JSON)
- Parquet Files
- Snowflake Storage Integrations
