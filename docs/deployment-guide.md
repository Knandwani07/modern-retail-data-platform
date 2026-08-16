# 🚀 Deployment Guide

This document outlines the infrastructure and services that must be deployed to build the retail data platform.

---

## Components Deployed

### AWS Resources

- Amazon S3 Data Lake
- AWS IAM Roles and Policies
- AWS Glue ETL Job
- AWS Glue Crawler
- Amazon Athena
- AWS Lambda

### Snowflake Resources

- Database
- Schema
- Warehouse
- Storage Integration
- File Formats
- External Stages
- Tables

---

## Deployment Order

### 1. Create the S3 Data Lake

Deploy:

- S3 Bucket
- Raw Layer
- Curated Layer
- Athena Results Location

Purpose:

Store source and transformed datasets.

---

### 2. Configure IAM

Deploy:

- Glue IAM Role
- Lambda IAM Role
- Snowflake IAM Role
- S3 Access Policies

Purpose:

Provide secure access between AWS services and Snowflake.

---

### 3. Upload Source Datasets

Deploy:

- Customers Dataset
- Orders Dataset
- Products Dataset

Purpose:

Provide the source data for the pipeline.

---

### 4. Deploy AWS Glue Resources

Deploy:

- Glue Database
- Glue Crawler
- Glue ETL Job

Purpose:

Transform raw order data into curated Parquet datasets.

---

### 5. Deploy Athena Resources

Deploy:

- Athena Database
- Athena Tables

Purpose:

Enable serverless querying of curated data.

---

### 6. Deploy Lambda Automation

Deploy:

- trigger-retail-pipeline Function

Purpose:

Trigger Glue ETL jobs automatically.

---

### 7. Deploy Snowflake Environment

Deploy:

- retail_pipeline Database
- raw Schema
- retail_wh Warehouse

Purpose:

Provide the analytics environment.

---

### 8. Configure Snowflake-S3 Connectivity

Deploy:

- Storage Integration
- Trust Policy
- S3 Read Permissions

Purpose:

Allow Snowflake to securely access S3 data.

---

### 9. Deploy Snowflake Data Objects

Deploy:

- File Formats
- External Stages
- Raw Tables
- Curated Tables

Purpose:

Prepare Snowflake for data ingestion.

---

## Deployment Complete

After all resources are deployed:

- AWS data pipeline is operational.
- Snowflake can access S3.
- Data can be loaded and analyzed.
