import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Create directory if not exists
os.makedirs('data/raw', exist_ok=True)

np.random.seed(42)

NUM_CUSTOMERS = 2500
NUM_PRODUCTS = 150
NUM_STORES = 25
NUM_TRANSACTIONS = 105000

categories_segment = ['Consumer', 'Corporate', 'Home Office']
regions = ['North America', 'EMEA', 'APAC', 'LATAM']

customers_df = pd.DataFrame({
    'customer_id': [f'CUST-{1000+i}' for i in range(NUM_CUSTOMERS)],
    'customer_name': [f'Customer_{i}' for i in range(NUM_CUSTOMERS)],
    'segment': np.random.choice(categories_segment, size=NUM_CUSTOMERS, p=[0.5, 0.3, 0.2]),
    'region': np.random.choice(regions, size=NUM_CUSTOMERS)
})

categories = ['Electronics', 'Furniture', 'Office Supplies', 'Apparel']
products_df = pd.DataFrame({
    'product_id': [f'PROD-{500+i}' for i in range(NUM_PRODUCTS)],
    'product_name': [f'Item_{i}' for i in range(NUM_PRODUCTS)],
    'category': np.random.choice(categories, size=NUM_PRODUCTS),
    'unit_price': np.round(np.random.uniform(10.0, 1200.0, size=NUM_PRODUCTS), 2)
})

stores_df = pd.DataFrame({
    'store_id': [f'STR-{10+i}' for i in range(NUM_STORES)],
    'store_name': [f'Store_Branch_{i}' for i in range(NUM_STORES)],
    'region': np.random.choice(regions, size=NUM_STORES)
})

start_date = datetime(2023, 1, 1)
date_list = [start_date + timedelta(days=int(i)) for i in np.random.randint(0, 730, size=NUM_TRANSACTIONS)]

fact_sales_df = pd.DataFrame({
    'transaction_id': [f'TXN-{100000+i}' for i in range(NUM_TRANSACTIONS)],
    'order_date': date_list,
    'customer_id': np.random.choice(customers_df['customer_id'], size=NUM_TRANSACTIONS),
    'product_id': np.random.choice(products_df['product_id'], size=NUM_TRANSACTIONS),
    'store_id': np.random.choice(stores_df['store_id'], size=NUM_TRANSACTIONS),
    'quantity': np.random.randint(1, 10, size=NUM_TRANSACTIONS),
    'discount': np.round(np.random.choice([0.0, 0.05, 0.10, 0.15, 0.20], size=NUM_TRANSACTIONS, p=[0.5, 0.2, 0.15, 0.1, 0.05]), 2)
})

fact_sales_df = fact_sales_df.merge(products_df[['product_id', 'unit_price']], on='product_id', how='left')
fact_sales_df['gross_amount'] = fact_sales_df['quantity'] * fact_sales_df['unit_price']
fact_sales_df['net_amount'] = np.round(fact_sales_df['gross_amount'] * (1 - fact_sales_df['discount']), 2)
fact_sales_df.drop(columns=['unit_price'], inplace=True)

fact_sales_df.loc[fact_sales_df.sample(frac=0.015).index, 'discount'] = np.nan
duplicate_rows = fact_sales_df.sample(n=500)
fact_sales_df = pd.concat([fact_sales_df, duplicate_rows], ignore_index=True)

customers_df.to_csv('data/raw/dim_customers.csv', index=False)
products_df.to_csv('data/raw/dim_products.csv', index=False)
stores_df.to_csv('data/raw/dim_stores.csv', index=False)
fact_sales_df.to_csv('data/raw/fact_sales.csv', index=False)

print("SUCCESS: Data files generated successfully!")