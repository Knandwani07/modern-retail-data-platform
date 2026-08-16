# 📥 Data Loading

This folder contains the Snowflake SQL commands used to connect Amazon S3 data sources, create staging objects, load datasets, and validate data ingestion.

The resources in this folder enable Snowflake to access raw and curated retail datasets stored in Amazon S3 and load them into Snowflake tables for analytics and reporting.

---

## 📄 Files

| File | Description |
|--------|-------------|
| `create-json-file-format.md` | Creates the JSON file format used to read raw product data stored in Amazon S3. |
| `create-products-stage.md` | Creates an external stage pointing to the raw product data location in Amazon S3. |
| `connect-products-s3-stage.md` | Configures the connection between Snowflake and the product data stage. |
| `verify-products-stage-access.md` | Verifies that Snowflake can successfully access files stored in the product stage. |
| `create-products-raw-table.md` | Creates the raw products table used to store semi-structured JSON product data. |
| `load-products-into-raw-table.md` | Loads product JSON files from Amazon S3 into the raw products table. |
| `validate-products-load.md` | Validates that product records were loaded successfully into Snowflake. |
| `load-products-json-data.md` | Queries and explores the loaded product JSON data. |
| `create-orders-curated-table.md` | Creates the curated orders table used to store transformed retail order data. |
| `load-curated-orders-data.md` | Loads curated order data from Amazon S3 into Snowflake for analytics. |

---

## 🎯 Purpose

The files in this folder are used to:

- Access raw and curated datasets stored in Amazon S3.
- Create Snowflake stages and file formats.
- Load semi-structured and structured data into Snowflake.
- Validate successful data ingestion.
- Prepare datasets for transformations and analytics.

---

## 🔄 Data Loading Workflow

1. Create the JSON file format.
2. Create and configure the products stage.
3. Verify stage connectivity.
4. Create the raw products table.
5. Load product JSON data into Snowflake.
6. Validate product data ingestion.
7. Create the curated orders table.
8. Load curated order data from Amazon S3.
9. Verify that all datasets are available for analytics.

---

## 🔧 Components Covered

- Snowflake External Stages
- Snowflake File Formats
- Snowflake Tables
- Amazon S3
- JSON Data Loading
- Curated Data Loading

---

## 📌 Notes

- Ensure the storage integration is configured before executing these commands.
- Verify stage access before loading any data.
- Validate record counts after each load operation to confirm successful ingestion.
- These datasets serve as the foundation for downstream transformations and analytics.
