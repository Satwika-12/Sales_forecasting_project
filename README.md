# Cloud-Based Sales Forecasting & Enterprise Analytics Dashboard

## Project Overview
An end-to-end Data Analytics and Predictive Modeling project that analyzes historical retail transactional data in Snowflake Data Warehouse, creates aggregated business analytics views, and leverages Machine Learning to forecast 30-day future sales revenue.

## Tech Stack & Skills
* **Languages & Analytics:** Python (Pandas, Scikit-Learn, Snowflake Connector)
* **Data Warehousing & SQL:** Snowflake (SQL Aggregations, Business Views, Joins)
* **Data Sources:** Multi-table Retail Dataset (`RAW_CUSTOMERS`, `RAW_PRODUCTS`, `RAW_STORES`, `RAW_FACT_SALES`)
* **Predictive Modeling:** Linear Regression (Sales Forecasting)
* **Tools:** VS Code, Git, PowerShell

## Key Project Milestones
1. **Data Ingestion & Integration:** Integrated multi-table retail transactional data into Snowflake Data Warehouse.
2. **Data Transformation & Aggregation:** Modeled SQL views (`VIEW_MASTER_SALES_ANALYTICS`, `VIEW_DAILY_SALES_SUMMARY`) to synthesize key metrics across customer segments, regions, and sales trends.
3. **Exploratory Data Analysis (EDA):** Analyzed **730 daily transaction records** to evaluate net revenue performance and discount impact.
4. **Predictive Analytics:** Implemented a Scikit-Learn regression model to predict daily net revenue for the next 30 days (`forecast_output.csv`).

## Key Results & Insights
* Derived continuous business performance metrics over a **2-year (730-day) dataset**.
* Successfully forecasted a 30-day sales revenue trend to enable data-driven business planning.