import pandas as pd
import numpy as np
import snowflake.connector
from sklearn.linear_model import LinearRegression

# 1. Connect to Snowflake & Fetch Aggregated View Data
conn = snowflake.connector.connect(
    user='satwika12',
    password='Satwika12345678',
    account='ijgymox-uk74925',
    warehouse='SALES_WH',
    database='SALES_ENTERPRISE_DB',
    schema='RAW_STAGE'
)

query = "SELECT ORDER_DATE, TOTAL_NET_REVENUE FROM VIEW_DAILY_SALES_SUMMARY ORDER BY ORDER_DATE ASC"
df = pd.read_sql(query, conn)
conn.close()

print(f"Data fetched successfully! Total days of data: {len(df)}")

# 2. Data Preparation for ML Model
df['ORDER_DATE'] = pd.to_datetime(df['ORDER_DATE'])
df = df.sort_values('ORDER_DATE')
df['DAY_INDEX'] = np.arange(len(df))

X = df[['DAY_INDEX']]
y = df['TOTAL_NET_REVENUE']

# 3. Train Sales Forecasting Model
model = LinearRegression()
model.fit(X, y)
print("Model trained successfully!")

# 4. Predict Next 30 Days Sales
future_days = 30
last_day_index = df['DAY_INDEX'].max()
future_indices = np.arange(last_day_index + 1, last_day_index + 1 + future_days).reshape(-1, 1)

future_predictions = model.predict(future_indices)

last_date = df['ORDER_DATE'].max()
future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=future_days)

forecast_df = pd.DataFrame({
    'ORDER_DATE': future_dates,
    'FORECASTED_REVENUE': future_predictions
})

print("\n--- NEXT 30 DAYS SALES FORECAST PREVIEW ---")
print(forecast_df.head())

# Save forecast locally
forecast_df.to_csv('data/raw/forecast_output.csv', index=False)
print("\nForecast data saved to data/raw/forecast_output.csv successfully!")