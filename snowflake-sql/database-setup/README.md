# 🏗️ Database Setup

This folder contains the Snowflake SQL commands required to create the foundational resources for the retail analytics platform.

These resources establish the database environment where retail data is stored, processed, and analyzed. The setup includes the database, schema, and virtual warehouse used throughout the project.

---

## 📄 Files

| File | Description |
|--------|-------------|
| `create-database.md` | Creates the primary Snowflake database used to store retail analytics data and objects. |
| `create-schema.md` | Creates the schema used to organize tables, stages, file formats, and other database objects. |
| `create-warehouse.md` | Creates the Snowflake virtual warehouse that provides compute resources for data loading, transformations, and analytics queries. |

---

## 🎯 Purpose

The files in this folder are used to:

- Create the core Snowflake environment.
- Organize project resources within a dedicated schema.
- Provision compute resources for query execution.
- Prepare Snowflake for data ingestion from Amazon S3.
- Establish the foundation for analytics and reporting workflows.

---

## 🔄 Setup Workflow

1. Create the Snowflake database.
2. Create the schema within the database.
3. Create and configure the virtual warehouse.
4. Verify that all resources are available before proceeding with storage integration and data loading.

---

## 🔧 Components Covered

- Snowflake Database
- Snowflake Schema
- Snowflake Virtual Warehouse

---

## 📌 Notes

- Execute these SQL commands before configuring storage integrations or external stages.
- The warehouse size can be adjusted based on workload requirements.
- Ensure you have sufficient Snowflake privileges to create databases, schemas, and warehouses.
