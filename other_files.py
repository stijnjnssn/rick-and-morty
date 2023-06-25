import configparser
import requests
import pandas as pd
from datetime import datetime

def second_ex_first_question():

    # Read the configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Extract the username, password, and URL base
    username = config.get('Credentials', 'username')
    password = config.get('Credentials', 'password')
    url_base = config.get('URL', 'url_base')

    # Check if the provided username and password match the config file
    if username == 'dummy_username' and password == 'dummy_password':
        url_query = "api/currencies"
        full_url = url_base + url_query

        response = requests.get(full_url)
        data = response.json()

        # Create a DataFrame from the API response
        df = pd.DataFrame(data)

        df_new = pd.DataFrame(df['data']['currencies']).transpose()
        print(df_new.head())

        # Filter rows where "altcoing" == False
        df_currency_code = df_new[df_new['altcoin'] == False]

        # Display the filtered DataFrame in tabular format
        print(df_currency_code)

        # Keep the DataFrame in memory for further use
        # You can access it using the name "df_currency_code"
    else:
        print('Authentication failed. Unable to make the API call.')

def second_exercise_second_question():

    # Get the current timestamp
    time_api_call = datetime.now()

    # Make the API call
    url_base = 'https://localbitcoins.com/'
    url = "bitcoinaverage/ticker-all-currencies/"
    complete_url = url_base + url
    response = requests.get(complete_url)

    # Check if the response is valid JSON --> never worked!
    try:
        data = response.json()
    except ValueError as e:
        print("Error: Invalid JSON response from the API")
        print("Details:", e)
        data = {}

    # Create a DataFrame if data is not empty
    if data:
        """
        I have written this part without having any validation since the API call doesnt work,
         but it should work if data is provided. 
         (Basic panda functionalities)
         """

        # Create a DataFrame
        df_price = pd.DataFrame(data)

        # Add a timestamp column with the value from time_api_call
        df_price['timestamp'] = time_api_call

        # Display the DataFrame
        print(df_price)

        """
        pd.merge() is used to merge df_currency and df_price based on their index. The merged DataFrame is stored in df_final.

        To review data quality, df_final.info() displays information about the DataFrame, including data types. df_final.isna().sum() shows the count of NaN values in each column, and df_final.duplicated().sum() returns the number of duplicate rows.
        
        Next, the timestamp column is set as the index using pd.to_datetime() to convert it to a datetime data type. The column is then dropped from the DataFrame.
        
        resample_data() is defined to resample the dataset by a given period of time. It uses the resample() method from pandas to resample the data and computes the mean for each period.
        
        Finally, the resample_data() function is applied to df_final with a period of 'T' (minutes) to obtain df_resampled, which contains the resampled data on a minute frequency.
        """

        # Merge df_currency with df_price
        df_final = pd.merge(df_currency, df_price, left_index=True, right_index=True)

        # Review data quality
        print(df_final.info())
        print(df_final.isna().sum())
        print(df_final.duplicated().sum())

        # Define timestamp index
        df_final.index = pd.to_datetime(df_final['timestamp'])
        df_final = df_final.drop(columns='timestamp')

        # Resample the dataset on frequency by minute
        df_resampled = resample_data(df_final, 'T')

# Function to resample dataset by a given period of time
    def resample_data(df, period):
        return df.resample(period).mean()