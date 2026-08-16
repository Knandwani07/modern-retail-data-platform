# 🏗️ Architecture Overview

The Modern Retail Data Platform combines AWS analytics services and Snowflake to create a scalable retail analytics solution.

The platform uses Amazon S3 as the central data lake where raw retail datasets are stored. AWS Glue automatically discovers datasets, performs transformations, and generates curated Parquet files for analytics workloads.

Amazon Athena provides serverless querying capabilities on the curated dataset, while Snowflake consumes selected datasets through external stages for additional reporting and analysis.

---

## Data Flow

### 1. Data Ingestion

Retail datasets are uploaded into Amazon S3.

```text
raw/
├── customers/
├── products/
└── orders/
```

---

### 2. Metadata Discovery

AWS Glue Crawlers scan the S3 locations and create metadata within the Glue Data Catalog.

```text
Amazon S3
    ↓
AWS Glue Crawler
    ↓
Glue Data Catalog
```

---

### 3. Data Transformation

The AWS Glue ETL job processes raw order data and creates curated Parquet files.

```text
Raw Data
    ↓
Glue ETL Job
    ↓
Curated Parquet Data
```

---

### 4. Analytics with Athena

Amazon Athena queries the curated dataset directly from Amazon S3 using metadata stored in the Glue Data Catalog.

```text
Curated Data
    ↓
Glue Data Catalog
    ↓
Amazon Athena
```

---

### 5. Snowflake Batch Loading

Snowflake connects to Amazon S3 through storage integrations and external stages.

```text
Amazon S3
    ↓
Snowflake External Stage
    ↓
Snowflake Landing Tables
    ↓
Snowsight Queries
```

---

## Architecture Characteristics

- Event-driven ingestion
- Automated ETL processing
- Serverless analytics
- Centralized metadata management
- Secure cross-account Snowflake integration
- Hybrid AWS and Snowflake analytics architecture
