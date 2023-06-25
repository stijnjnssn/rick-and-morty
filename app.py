import time
import pandas as pd
import requests
from sqlalchemy import create_engine

# Define API URL and other variables
url_base = 'https://localbitcoins.com/'
url = 'bitcoinaverage/ticker-all-currencies/'
db_url = 'postgresql://username:password@localhost:xxxxx'  # Replace with your PostgreSQL connection URL --> didn't do this since api call doesnt work
parquet_file = 'df_final.parquet'

# Function to call the API and create df_final
def call_api():
    # Make API call
    response = requests.get(url_base + url)
    data = response.json()

    # Get current time
    time_api_call = pd.Timestamp.now()

    # Create DataFrame from API response
    df_price = pd.DataFrame.from_dict(data, orient='index', columns=['price'])
    df_price['timestamp'] = time_api_call

    # Load existing df_final from parquet file (if it exists)
    try:
        df_final = pd.read_parquet(parquet_file)
    except FileNotFoundError:
        df_final = pd.DataFrame()

    # Append new data to df_final
    df_final = pd.concat([df_final, df_price])

    # Save df_final to parquet file
    df_final.to_parquet(parquet_file)

    # Connect to the PostgreSQL database
    engine = create_engine(db_url)

    # Append df_final to the PostgreSQL table
    df_final.to_sql('table_name', engine, if_exists='append')

# Call the API every 10 minutes
while True:
    call_api()
    time.sleep(600)  # Sleep for 10 minutes (600 seconds)
