# ❄️ Snowflake SQL

This directory contains the Snowflake SQL scripts used to build, configure, and operate the Snowflake environment for the Modern Retail Data Platform.

The scripts cover database provisioning, storage integration with Amazon S3, data loading, and data transformation activities required to prepare retail datasets for analytics and reporting.

---

## 📂 Directory Structure

| Folder | Purpose |
|----------|---------|
| `database-setup/` | Creates the foundational Snowflake resources including the database, schema, and virtual warehouse. |
| `storage-integration/` | Configures secure connectivity between Snowflake and Amazon S3 using storage integrations, file formats, and external stages. |
| `data-loading/` | Creates tables, stages, and file formats required to load raw and curated retail datasets into Snowflake. |
| `transformations/` | Contains SQL transformations used to prepare and normalize data for downstream analytics and reporting. |

---

## 🎯 Objectives

The SQL scripts in this directory are used to:

- Provision Snowflake infrastructure.
- Establish secure access to Amazon S3.
- Load raw and curated retail datasets.
- Process semi-structured JSON data.
- Transform datasets into analytics-ready formats.
- Support reporting and business intelligence workflows.

---

## 🔄 Implementation Flow

The folders should be executed in the following order:

### 1. Database Setup

Create the foundational Snowflake resources:

- Database
- Schema
- Virtual Warehouse

### 2. Storage Integration

Configure Snowflake access to Amazon S3:

- Storage Integration
- File Formats
- External Stages
- Access Validation

### 3. Data Loading

Load retail datasets into Snowflake:

- Product JSON Data
- Curated Order Data
- Validation Queries

### 4. Transformations

Apply data transformations:

- Flatten Product Tags
- Prepare analytics-ready datasets

---

## 🔧 Snowflake Features Used

- Databases
- Schemas
- Virtual Warehouses
- Storage Integrations
- External Stages
- File Formats
- Tables
- VARIANT Data Type
- COPY INTO Commands
- FLATTEN Function

---

## 📌 Notes

- Execute the folders sequentially to avoid dependency issues.
- Ensure AWS IAM roles and Snowflake storage integrations are configured before loading data.
- Replace placeholder values such as bucket names, IAM role ARNs, and account-specific identifiers before execution.
- Validate data ingestion before running transformations and analytics queries.
