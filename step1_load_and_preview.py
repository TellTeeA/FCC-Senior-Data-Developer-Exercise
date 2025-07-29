import pandas as pd
import os

# Set the path to raw data folder
data_path = os.path.join(os.getcwd(), 'raw_data')

# File mapping
file_names = {
    "user": "user.csv",
    "user_registration": "user_registration.csv",
    "plan": "plan.csv",
    "plan_payment_frequency": "plan_payment_frequency.csv",
    "user_plan": "user_plan.csv",
    "user_payment_detail": "user_payment_detail.csv",
    "user_play_session": "user_play_session.csv",
    "status_code": "status_code.csv",
    "channel_code": "channel_code.csv"
}

# Load data
dataframes = {}
for name, file in file_names.items():
    full_path = os.path.join(data_path, file)
    dataframes[name] = pd.read_csv(full_path)

# Preview 2 rows from each
for name, df in dataframes.items():
    print(f"--- {name.upper()} ---")
    print(df.head(2))
    print("\n")



