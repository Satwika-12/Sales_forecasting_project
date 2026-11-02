-- 1. Create Enterprise Database & Warehouse
CREATE DATABASE IF NOT EXISTS SALES_ENTERPRISE_DB;
CREATE WAREHOUSE IF NOT EXISTS SALES_WH WITH WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 300 AUTO_RESUME = TRUE;

USE DATABASE SALES_ENTERPRISE_DB;
USE WAREHOUSE SALES_WH;

-- 2. Create RAW Schema for Staging Data
CREATE SCHEMA IF NOT EXISTS RAW_STAGE;
USE SCHEMA RAW_STAGE;

-- 3. Create RAW Fact & Dimension Tables
CREATE OR REPLACE TABLE RAW_CUSTOMERS (
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    region VARCHAR(50)
);

CREATE OR REPLACE TABLE RAW_PRODUCTS (
    product_id VARCHAR(50),
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price NUMBER(10, 2)
);

CREATE OR REPLACE TABLE RAW_STORES (
    store_id VARCHAR(50),
    store_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE OR REPLACE TABLE RAW_FACT_SALES (
    transaction_id VARCHAR(50),
    order_date VARCHAR(50),
    customer_id VARCHAR(50),
    product_id VARCHAR(50),
    store_id VARCHAR(50),
    quantity NUMBER(10, 0),
    discount NUMBER(5, 2),
    gross_amount NUMBER(12, 2),
    net_amount NUMBER(12, 2)
);