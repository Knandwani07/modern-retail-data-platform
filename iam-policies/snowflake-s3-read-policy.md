# 📦 Snowflake S3 Read Policy

## 📖 Overview

This policy grants Snowflake permission to access curated data stored in Amazon S3 through the `SnowflakeS3AccessRole`.

Once the trust relationship between AWS and Snowflake has been established, this policy allows Snowflake to list objects within the designated S3 bucket and read the curated Parquet files used for analytics and data warehousing.

---

## 🎯 Purpose

This policy is required to:

- Allow Snowflake to read data stored in Amazon S3.
- Allow Snowflake to list objects within the data lake bucket.
- Support external stages and storage integrations.
- Enable loading curated datasets from AWS into Snowflake.

---

## 🔗 Attached To

```text
SnowflakeS3AccessRole
```

---

## ⚙️ Used By

```text
Snowflake Storage Integration (retail_s3_int)
```

---

## 🔐 Permissions Granted

| Permission | Description |
|------------|-------------|
| `s3:GetObject` | Read objects stored in Amazon S3 |
| `s3:GetObjectVersion` | Read specific object versions |
| `s3:ListBucket` | List objects within the S3 bucket |

---

## 📄 Policy Document

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
      "Resource": "arn:aws:s3:::retail-pipeline-yourname-2026/curated/*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::retail-pipeline-yourname-2026"
    }
  ]
}
```

---

## 📋 Configuration Steps

1. Navigate to **IAM → Roles → SnowflakeS3AccessRole**.
2. Click **Add permissions → Create inline policy**.
3. Open the **JSON** editor.
4. Replace the existing content with the policy shown above.
5. Update the S3 bucket ARN values to match your environment.
6. Create the policy using the name:

```text
SnowflakeS3ReadPolicy
```

7. Verify that the policy is attached successfully.
8. Confirm that the role can list bucket contents and read objects from the curated data location.

---

## 🔄 How It Works

1. Snowflake assumes the `SnowflakeS3AccessRole`.
2. The role receives temporary AWS credentials.
3. Snowflake lists files within the configured S3 location.
4. Snowflake reads Parquet files from the curated layer.
5. The data becomes available for querying and loading within Snowflake.

---

## 💡 Why This Policy Is Important

Without this policy, Snowflake can establish trust with AWS but cannot access any data stored in Amazon S3.

This policy provides the minimum permissions required for Snowflake to discover and read curated datasets while maintaining controlled access to the data lake.

---

## 🏗️ Services Involved

- Amazon S3
- AWS IAM
- Snowflake
- Snowflake Storage Integration
