# 🔄 Data Transformations

This folder contains the data transformation logic used within the retail analytics platform.

The transformations are applied to raw datasets to improve data usability, support analytics requirements, and prepare the data for downstream reporting in Athena and Snowflake.

---

## 📄 Files

| File | Description |
|--------|-------------|
| `flatten-product-tags.md` | Documents the transformation used to flatten the nested product tags array into individual rows for easier querying and analysis. |

---

## 🎯 Purpose

The transformations in this folder help:

- Convert semi-structured data into an analytics-friendly format.
- Simplify SQL queries and reporting workflows.
- Improve compatibility with Snowflake and Athena.
- Prepare retail datasets for business intelligence and visualization.

---

## 🔧 Transformation Covered

### Product Tag Flattening

The product dataset contains a nested array of tags for each product. The flattening process expands the array into individual records, allowing each tag to be analyzed independently.

This transformation enables:

- Product categorization analysis
- Tag-based filtering and reporting
- Improved search and aggregation capabilities
- Easier downstream analytics

---

## 📌 Notes

- Transformations documented in this folder are applied after data ingestion.
- The resulting datasets are optimized for analytics and reporting workloads.
- Additional transformations can be added as the platform evolves.
