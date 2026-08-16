# 🔍 Athena Queries

This folder contains the Amazon Athena SQL query used to validate the curated retail dataset stored in Amazon S3.

---

## 📁 Query Overview

| File | Purpose |
|--------|---------|
| `validation-query.md` | Validates the curated dataset by checking the total number of records and distinct orders. |

---

## 🎯 Purpose

The validation query is used to:

- Confirm that the curated dataset was loaded successfully.
- Check the total number of records.
- Verify the number of distinct orders.
- Identify potential duplicate order records.

This provides a basic data-quality check before the curated dataset is used for further analysis in Snowflake.
