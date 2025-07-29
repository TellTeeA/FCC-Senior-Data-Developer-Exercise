import pandas as pd
import os

# Load source files
raw_path = os.path.join(os.getcwd(), 'raw_data')
proc_path = os.path.join(os.getcwd(), 'processed_data')

sessions = pd.read_csv(os.path.join(raw_path, 'user_play_session.csv'))
dim_user = pd.read_csv(os.path.join(proc_path, 'dim_user.csv'))
dim_channel = pd.read_csv(os.path.join(proc_path, 'dim_channel.csv'))
dim_status = pd.read_csv(os.path.join(proc_path, 'dim_status.csv'))

# Rename for joining
dim_channel = dim_channel.rename(columns={"channel_code": "join_channel_code"})
dim_status = dim_status.rename(columns={"status_code": "join_status_code"})

# Join user info
fact_table = pd.merge(sessions, dim_user[['user_id', 'user_registration_id']], on='user_id', how='left')

# Join channel and status descriptions
fact_table = pd.merge(fact_table, dim_channel, left_on='channel_code', right_on='join_channel_code', how='left')
fact_table = pd.merge(fact_table, dim_status, left_on='status_code', right_on='join_status_code', how='left')

# Drop technical join columns
fact_table.drop(columns=['join_channel_code', 'join_status_code'], inplace=True)

# Save to CSV
fact_table.to_csv(os.path.join(proc_path, 'fact_user_play_session.csv'), index=False)

print("✅ Fact table created and saved to 'processed_data/fact_user_play_session.csv'")
