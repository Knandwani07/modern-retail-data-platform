## 📈 Building a Modern Retail Data Platform on AWS and Snowflake

### 📖 About this Project

The **Modern Retail Data Platform on AWS and Snowflake** demonstrates how to build a cloud-native retail analytics solution using AWS data services and Snowflake.

The platform ingests retail sales data into Amazon S3, automatically catalogs and transforms data using AWS Glue, and enables analytics through Amazon Athena. Curated datasets are also made available to Snowflake through secure storage integrations and external stages, allowing additional querying and analysis using Snowsight.

The project showcases a complete modern data pipeline that combines automated AWS data lake processing with Snowflake-based analytics using structured and semi-structured datasets.

---

### 🎯 Project Objectives

* Build a centralized retail data lake using Amazon S3.
* Automate metadata discovery using AWS Glue Crawlers.
* Transform raw retail data into curated Parquet datasets.
* Maintain a centralized metadata catalog using AWS Glue Data Catalog.
* Query curated datasets using Amazon Athena.
* Implement event-driven pipeline automation with AWS Lambda.
* Secure data access using IAM roles and policies.
* Integrate Amazon S3 with Snowflake using Storage Integrations.
* Load structured and semi-structured datasets into Snowflake.
* Analyze retail sales performance using SQL and visualizations.
* Demonstrate modern data engineering and analytics workflows on AWS and Snowflake.

---

### 📂 Project Structure

```text
modern-retail-data-platform/
│
├── analytics/
│   ├── README.md
│   ├── category-revenue-analysis.md
│   ├── order-distribution-by-category.md
│   └── top-revenue-products.md
│
├── architecture/
│   ├── README.md
│   ├── architecture-components.md
│   └── architecture-overview.md
│
├── athena-queries/
│   ├── README.md
│   └── validation-query.md
│
├── docs/
│   ├── README.md
│   ├── cleanup-guide.md
│   ├── deployment-guide.md
│   └── execution-workflow.md
│
├── iam-policies/
│   ├── README.md
│   ├── glue-retail-s3-access-policy.md
│   ├── lambda-start-glue-job-policy.md
│   ├── snowflake-s3-read-policy.md
│   ├── snowflake-s3-read-policy-update.md
│   └── snowflake-trust-policy.md
│
├── pipeline-automation/
│   ├── README.md
│   ├── lambda_test_s3_event.json
│   └── lambda_trigger_pipeline.py
│
├── sample-data/
│   ├── README.md
│   ├── customers.csv
│   ├── orders.parquet
│   └── products.json
│
├── snowflake-sql/
│   ├── README.md
│   │
│   ├── database-setup/
│   │   ├── README.md
│   │   ├── create-database.md
│   │   ├── create-schema.md
│   │   └── create-warehouse.md
│   │
│   ├── storage-integration/
│   │   ├── README.md
│   │   ├── create-storage-integration.md
│   │   ├── describe-storage-integration.md
│   │   ├── create-parquet-file-format.md
│   │   ├── create-curated-stage.md
│   │   └── verify-stage-access.md
│   │
│   ├── data-loading/
│   │   ├── README.md
│   │   ├── create-json-file-format.md
│   │   ├── create-products-stage.md
│   │   ├── connect-products-s3-stage.md
│   │   ├── create-products-raw-table.md
│   │   ├── load-products-json-data.md
│   │   ├── load-products-into-raw-table.md
│   │   ├── validate-products-load.md
│   │   ├── create-orders-curated-table.md
│   │   ├── load-curated-orders-data.md
│   │   └── verify-products-stage-access.md
│   │
│   └── transformations/
│       ├── README.md
│       └── flatten-product-tags.md
│
├── bucket-structure.md
└── README.md
```

---

### 📄 File Description

| Folder / File            | Description                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| **analytics/**           | Business analysis and visualization documentation created from the curated retail dataset.             |
| **architecture/**        | Architecture diagrams, workflow explanations, and infrastructure component documentation.              |
| **athena-queries/**      | Amazon Athena SQL queries used for dataset validation and verification.                                |
| **docs/**                | Deployment, execution workflow, and cleanup documentation for the project.                             |
| **iam-policies/**        | IAM policies and trust relationships required for AWS Glue, Lambda, and Snowflake integration.         |
| **pipeline-automation/** | AWS Lambda automation code and test events used to trigger the data pipeline.                          |
| **sample-data/**         | Sample retail datasets used throughout the project.                                                    |
| **snowflake-sql/**       | Snowflake SQL scripts used for database setup, storage integration, data loading, and transformations. |
| **bucket-structure.md**  | Documents the Amazon S3 data lake folder structure and its purpose.                                    |
| **README.md**            | Main project documentation and repository guide.                                                       |

---

### 🏗️ Core AWS Services Used

* Amazon S3
* AWS Glue Crawlers
* AWS Glue ETL
* AWS Glue Data Catalog
* AWS Lambda
* Amazon Athena
* AWS Lake Formation
* AWS IAM
* Amazon CloudWatch

---

### ❄️ Snowflake Components Used

* Snowflake Warehouse
* Snowflake Database & Schema
* Storage Integrations
* External Stages
* File Formats
* Landing Tables
* Snowsight Worksheets
* Semi-Structured Data (VARIANT)

---

### 📊 Analytics Generated

The platform produces several business insights from the curated retail dataset:

* Revenue by Product Category
* Top Revenue-Generating Products
* Order Distribution by Category
* Dataset Validation Metrics

These analytics demonstrate how curated retail data can be transformed into actionable business intelligence.

---

### 📚 Concepts Covered

* Data Lakes
* ETL Pipelines
* Data Cataloging
* Event-Driven Architecture
* Serverless Data Processing
* Data Governance
* Data Warehousing
* Snowflake External Stages
* Semi-Structured Data Processing
* Retail Analytics
* Cloud Data Engineering
* Business Intelligence Reporting

---

### 🤝 Let's Connect

- 💼 **LinkedIn:** https://www.linkedin.com/in/khushi-nandwani/
- 💻 **GitHub:** https://github.com/Knandwani07
- 📬 **Substack:** https://substack.com/@khushinandwani07
- ✍️ **Dev Community:** https://dev.to/khushi_nandwani07
- 📝 **Medium:** https://medium.com/@khushinandwanii
- 🌐 **Portfolio:** https://main.d1n4wt6uo5bfx6.amplifyapp.com/

---

⭐ **If you found this project helpful, consider giving it a star!**


---
