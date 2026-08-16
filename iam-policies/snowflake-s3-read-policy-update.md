# 📦 Snowflake S3 Read Policy Update

## 📖 Overview

As the project expands to include product data ingestion, the existing `SnowflakeS3ReadPolicy` must be updated to grant Snowflake access to both the curated Parquet datasets and the raw product JSON files stored in Amazon S3.

This policy update ensures that Snowflake can read data from multiple locations within the data lake while maintaining controlled access through IAM.

---

## 🎯 Purpose

This policy update is required to:

- Allow Snowflake to read curated Parquet datasets.
- Allow Snowflake to read raw product JSON datasets.
- Allow Snowflake to list files in approved S3 locations.
- Support external stages used for analytics and data ingestion.

---

## 🔗 Attached To

```text
SnowflakeS3AccessRole
```

---

## ⚙️ Used By

```text
retail_s3_int Storage Integration
curated_stage External Stage
products_stage External Stage
```

---

## 🔐 Updated Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectVersion"
      ],
      "Resource": [
        "arn:aws:s3:::<your-s3-bucket-name>/curated/*",
        "arn:aws:s3:::<your-s3-bucket-name>/raw/products/*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": "arn:aws:s3:::<your-s3-bucket-name>",
      "Condition": {
        "StringLike": {
          "s3:prefix": [
            "curated/*",
            "raw/products/*"
          ]
        }
      }
    }
  ]
}
```

---

## 📋 Configuration Steps

1. Navigate to **IAM → Roles → SnowflakeS3AccessRole**.
2. Open the **Permissions** tab.
3. Select the existing **SnowflakeS3ReadPolicy**.
4. Edit the policy and replace it with the updated version shown above.
5. Save the policy changes.
6. Verify that the policy is attached successfully to the role.
7. Confirm that permissions exist for both:
   - `curated/*`
   - `raw/products/*`

---

## 🔄 How It Works

1. Snowflake assumes the `SnowflakeS3AccessRole`.
2. The role receives temporary AWS credentials.
3. Snowflake can list files within approved S3 prefixes.
4. Snowflake can read:
   - Curated Parquet datasets
   - Raw product JSON datasets
5. Data becomes available for loading and transformation within Snowflake.

---

## 💡 Why This Policy Is Important

Without this update, Snowflake would only have access to the curated data layer and would be unable to read product JSON files stored in the raw layer.

This policy enables the next phase of the project, where semi-structured product data is loaded and transformed within Snowflake.

---

## 🏗️ Services Involved

- AWS IAM
- Amazon S3
- Snowflake
- Snowflake Storage Integration
- Snowflake External Stages

---

## 📁 Policy Location

```text
policies/
└── snowflake-s3-read-policy-update.md
```
