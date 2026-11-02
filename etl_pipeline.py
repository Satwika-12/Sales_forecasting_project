import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# 1. Snowflake Connection Setup
conn = snowflake.connector.connect(
    user='satwika12',                  # Nee Snowflake Username
    password='Satwika12345678',        # Nee Snowflake Password
    account='ijgymox-uk74925',         # Account identifier
    warehouse='SALES_WH',
    database='SALES_ENTERPRISE_DB',
    schema='RAW_STAGE'
)

print("Connected to Snowflake successfully!")

# 2. Local CSV Files Load Cheyadam
files_to_tables = {
    'data/raw/dim_customers.csv': 'RAW_CUSTOMERS',
    'data/raw/dim_products.csv': 'RAW_PRODUCTS',
    'data/raw/dim_stores.csv': 'RAW_STORES',
    'data/raw/fact_sales.csv': 'RAW_FACT_SALES'
}

# 3. Tables loki Push Cheyadam
for file_path, table_name in files_to_tables.items():
    print(f"Loading {file_path} into {table_name}...")
    df = pd.read_csv(file_path)
    
    # Column names uppercase ki covert chestam to match Snowflake schema
    df.columns = [col.upper() for col in df.columns]
    
    # Write DataFrame to Snowflake Table
    success, nchunks, nrows, _ = write_pandas(conn, df, table_name)
    print(f"Successfully loaded {nrows} rows into {table_name}.")

conn.close()
print("ALL DATA LOADED TO SNOWFLAKE SUCCESSFULLY!")