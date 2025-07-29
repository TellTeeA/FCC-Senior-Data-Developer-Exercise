import pandas as pd
import os

proc_path = os.path.join(os.getcwd(), 'processed_data')
raw_path = os.path.join(os.getcwd(), 'raw_data')

fact = pd.read_csv(os.path.join(proc_path, 'fact_user_play_session.csv'))
user_plan = pd.read_csv(os.path.join(raw_path, 'user_plan.csv'))
dim_plan = pd.read_csv(os.path.join(proc_path, 'dim_plan.csv'))

# 1. Channel distribution
channel_summary = fact['channel_code'].value_counts()

# 2. Total revenue (join plan_id with cost)
plan_join = pd.merge(user_plan, dim_plan, on='plan_id', how='left')
plan_join['cost_amount'] = plan_join['cost_amount'].fillna(0)
revenue_by_plan = plan_join.groupby('payment_frequency_code')['cost_amount'].sum()

# 3. Total gross revenue
total_revenue = plan_join['cost_amount'].sum()

# Output insights
print(" Sessions by Channel:")
print(channel_summary)

print("\n Revenue by Payment Type:")
print(revenue_by_plan)

print(f"\n Total Gross Revenue: ${total_revenue:,.2f}")

# Forecasting Placeholder
# Assume a 10% YoY growth for 2025
forecast_2025 = total_revenue * 1.10
print(f"\n Projected 2025 Revenue (10% Growth): ${forecast_2025:,.2f}")

