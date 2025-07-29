import pandas as pd
import os

# Load raw data
data_path = os.path.join(os.getcwd(), 'raw_data')
user = pd.read_csv(os.path.join(data_path, 'user.csv'))
user_reg = pd.read_csv(os.path.join(data_path, 'user_registration.csv'))
plan = pd.read_csv(os.path.join(data_path, 'plan.csv'))
plan_freq = pd.read_csv(os.path.join(data_path, 'plan_payment_frequency.csv'))
payment_detail = pd.read_csv(os.path.join(data_path, 'user_payment_detail.csv'))
channel_code = pd.read_csv(os.path.join(data_path, 'channel_code.csv'))
status_code = pd.read_csv(os.path.join(data_path, 'status_code.csv'))

# Create dim_user (merge reg and core info)
dim_user = pd.merge(user_reg, user, on='user_id', how='left')

# Rename to avoid email conflict
dim_user = dim_user.rename(columns={
    'email_x': 'registration_email',
    'email_y': 'user_email'
})

# Create full name
dim_user['full_name'] = dim_user['first_name'] + ' ' + dim_user['last_name']

# Final column list
dim_user = dim_user[['user_registration_id', 'user_id', 'username', 'registration_email', 'user_email', 'full_name', 'ip_address', 'social_media_handle']]


# Create dim_plan
dim_plan = pd.merge(plan, plan_freq, on='payment_frequency_code', how='left')
dim_plan = dim_plan[['plan_id', 'payment_frequency_code', 'english_description', 'cost_amount']]

# Create dim_payment_method
dim_payment_method = payment_detail.copy()
dim_payment_method = dim_payment_method[['payment_detail_id', 'payment_method_code', 'payment_method_value', 'payment_method_expiry']]

# Create dim_channel
dim_channel = channel_code.rename(columns={
    'play_session_channel_code': 'channel_code',
    'english_description': 'channel_description_en',
    'french_description': 'channel_description_fr'
})

# Create dim_status
dim_status = status_code.rename(columns={
    'play_session_status_code': 'status_code',
    'english_description': 'status_description_en',
    'french_description': 'status_description_fr'
})

# Save all dimension tables
output_path = os.path.join(os.getcwd(), 'processed_data')
os.makedirs(output_path, exist_ok=True)

dim_user.to_csv(os.path.join(output_path, 'dim_user.csv'), index=False)
dim_plan.to_csv(os.path.join(output_path, 'dim_plan.csv'), index=False)
dim_payment_method.to_csv(os.path.join(output_path, 'dim_payment_method.csv'), index=False)
dim_channel.to_csv(os.path.join(output_path, 'dim_channel.csv'), index=False)
dim_status.to_csv(os.path.join(output_path, 'dim_status.csv'), index=False)

print("Dimension tables saved to 'processed_data' folder.")
