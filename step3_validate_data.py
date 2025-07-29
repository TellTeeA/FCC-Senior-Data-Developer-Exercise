import pandas as pd
import os

path = os.path.join(os.getcwd(), 'processed_data')

# Load fact table
fact = pd.read_csv(os.path.join(path, 'fact_user_play_session.csv'))

print("Total Records:", len(fact))
print("Missing Values Per Column:")
print(fact.isnull().sum())

# Check date ranges
print("\n Start Date Range:", fact['start_datetime'].min(), "to", fact['start_datetime'].max())
print(" End Date Range:", fact['end_datetime'].min(), "to", fact['end_datetime'].max())

# Unique statuses and platforms
print("\n Session Statuses:", fact['status_code'].unique())
print(" Platforms:", fact['channel_code'].unique())

# Sample of invalid user_ids or scores
print("\n Any negative or zero scores?")
print(fact[fact['total_score'] <= 0].head())
