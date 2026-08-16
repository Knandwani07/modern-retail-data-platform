# AWS Glue S3 Access Policy

## Purpose

This policy grants AWS Glue permission to interact with the Amazon S3 data lake used in the retail analytics platform.

The policy enables AWS Glue Crawlers and ETL Jobs to:

- Read source datasets from Amazon S3.
- Write transformed datasets to Amazon S3.
- List bucket contents during crawling and processing.
- Delete objects when required.

## Attached To

```text
GlueRetailPipelineRole
```

## Used By

- AWS Glue Crawlers
- AWS Glue ETL Jobs

## Policy Document

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:ListBucket",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::retail-pipeline-yourname-2026",
        "arn:aws:s3:::529057333264/*"
      ]
    }
  ]
}
```

## Notes

This policy is included exactly as configured in the project implementation and is used to provide AWS Glue with access to the Amazon S3 data lake resources required for data ingestion and transformation workflows.
