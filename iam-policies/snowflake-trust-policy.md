# 🔐 Snowflake IAM Trust Policy

## 📖 Overview

This trust policy allows Snowflake to securely assume the AWS IAM role used for accessing data stored in Amazon S3.

After creating the Snowflake Storage Integration, Snowflake generates a unique IAM User ARN and External ID. These values must be added to the IAM role trust relationship so that Snowflake can authenticate and access the approved S3 locations.

---

## 🎯 Purpose

This policy is required to:

- Establish trust between AWS and Snowflake.
- Allow Snowflake to assume the `SnowflakeS3AccessRole`.
- Secure access to data stored in Amazon S3.
- Prevent unauthorized role assumption.

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

## 🔐 Trust Policy

Replace the placeholder values below with the values returned by:

```sql
DESC INTEGRATION retail_s3_int;
```

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "<STORAGE_AWS_IAM_USER_ARN>"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<STORAGE_AWS_EXTERNAL_ID>"
        }
      }
    }
  ]
}
```

---

## 📋 Configuration Steps

1. Navigate to **IAM → Roles** in the AWS Management Console.
2. Open the **SnowflakeS3AccessRole** role.
3. Select the **Trust relationships** tab.
4. Click **Edit trust policy**.
5. Replace the existing trust policy with the policy shown above.
6. Update the following placeholders using the values returned by `DESC INTEGRATION retail_s3_int`:
   - `STORAGE_AWS_IAM_USER_ARN`
   - `STORAGE_AWS_EXTERNAL_ID`
7. Save the updated trust policy.
8. Verify that the trust relationship has been updated successfully.

---

## 🔄 How It Works

1. Snowflake requests access to Amazon S3.
2. Snowflake uses the generated IAM User ARN and External ID.
3. AWS validates the trust relationship.
4. AWS allows Snowflake to assume the `SnowflakeS3AccessRole`.
5. Snowflake gains temporary credentials to access approved S3 locations.

---

## 💡 Why This Policy Is Important

Without this trust policy, Snowflake cannot assume the AWS IAM role and therefore cannot access data stored in Amazon S3.

This trust relationship provides a secure and controlled mechanism for integrating Snowflake with AWS while following security best practices.

---

## 🏗️ Services Involved

- AWS IAM
- Amazon S3
- Snowflake
- Snowflake Storage Integration
- AWS Security Token Service (STS)
