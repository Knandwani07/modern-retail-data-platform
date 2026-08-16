# 🧩 Architecture Components
<img width="1402" height="792" alt="arcdiagram" src="https://github.com/user-attachments/assets/75296fb2-24d5-47ab-a67e-b724819ce5ce" />


## Ingestion & Storage

### Amazon S3 (`retail-analytics-data-lake-pipeline-2026`)

Central data lake used to store all retail datasets.

Structure:

```text
raw/
├── customers/
├── products/
└── orders/

curated/

athena-results/
```

The same bucket is accessed by both AWS analytics services and Snowflake through different prefixes.

---

## Cataloging & Transformation (Automated)

### AWS Glue Crawler (Raw)

Scans the `raw/` dataset and creates metadata inside the Glue Data Catalog.

**Role:** `GlueRetailPipelineRole`

---

### AWS Glue ETL Job (`raw_to_curated`)

Transforms raw retail datasets and writes curated Parquet files into Amazon S3.

**Role:** `GlueRetailPipelineRole`

---

### AWS Glue Crawler (Curated)

Scans the curated data location and updates the `retail_curated` database in the Glue Data Catalog.

This crawler must be manually executed after each ETL run.

---

### AWS Glue Data Catalog

Central metadata repository used by AWS Glue and Amazon Athena.

Databases:

- `retail_raw`
- `retail_curated`

---

## Governance

### AWS Lake Formation

Provides centralized data access governance.

Configured to grant:

- SELECT access on `retail_curated.curated`

Granted to:

- `AnalystGlueAthenaAccessRole`

---

## Analytics

### Amazon Athena

Provides serverless SQL analytics on curated retail datasets.

Capabilities:

- Query curated Parquet data
- Generate business insights
- Store query outputs in `athena-results/`

**Role:** `AnalystGlueAthenaAccessRole`

---

## Automation Trigger

### Amazon S3 Event Notification

Monitors the following location:

```text
raw/orders/
```

Triggers AWS Lambda when new files arrive.

---

### AWS Lambda (`trigger-retail-pipeline`)

Automatically starts the AWS Glue ETL job when new order files are uploaded.

Responsibilities:

- Receive S3 event notifications
- Start Glue ETL job
- Log execution activity

Does not:

- Trigger Glue Crawlers
- Process customer uploads
- Process product uploads

---

## Identity & Access

### GlueRetailPipelineRole

Used by:

- AWS Glue Crawlers
- AWS Glue ETL Job

Permissions:

- Read from Amazon S3
- Write curated datasets to Amazon S3

---

### AnalystGlueAthenaAccessRole

Used for analytics access.

Permissions:

- Athena query execution
- Lake Formation permissions

---

### SnowflakeS3AccessRole

Cross-account IAM role trusted by Snowflake.

Permissions:

- Read `curated/`
- Read `raw/products/`

---

## Snowflake Integration

### Storage Integration (`retail_s3_int`)

Secure Snowflake object used to access Amazon S3 through IAM role delegation.

---

### External Stages

#### Curated Stage

Accesses:

```text
s3://.../curated/
```

Used to load curated order data.

---

#### Products Stage

Accesses:

```text
s3://.../raw/products/
```

Used to load raw product JSON data.

---

### Landing Tables

#### orders_curated

Stores structured retail order records.

#### products_raw

Stores semi-structured product JSON data using the VARIANT data type.

---

### Snowsight

Web-based SQL interface used for:

- Data loading
- Data validation
- Analytics queries

---

## Compute

### Snowflake Warehouse (`retail_wh`)

Configuration:

- Size: XSMALL
- Auto Suspend: 60 Seconds
- Auto Resume: Enabled

Provides compute resources for all Snowflake workloads.
