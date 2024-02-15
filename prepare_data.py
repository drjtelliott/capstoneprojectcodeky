import yfinance as yf
import pandas as pd
import os 

# Download Ticker Data

def download_data(ticker:str, start: str, end: str) -> pd.DataFrame: 
    print(f"Downloading {ticker} data....")

    # using yfinance download ticker information for particular date range
    data = yf.download(ticker, start=start, end=end)

    print(f"...{ticker} data downloaded")

    # return the pandas dataframe
    return data

def clean_data(data: pd.DataFrame) -> pd.DataFrame: 
    print("Cleaning data")

    # update data frame to only contain column we care about
    data = data.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'])

    # round the Close column to two decimal places
    data["Close"] = data["Close"].round(2)
 
    # # format the date column
    # data['Date'] = pd.to_datetime(data['Date'])

    # # format the date column to mm/dd/yyyy format
    # data['Date'] = data['Date'].dt.strftime('%m/%d/%Y')

    return data

def prepare_data(ticker:str, start: str, end: str, dir_name: str) -> pd.DataFrame: 
    print(f"Preparing data for {ticker}")

    data = download_data(ticker, start=start, end=end)
    data = clean_data(data)

    data.to_csv(f'{dir_name}/{ticker.lower()}_data.csv') 
    
    return data

def get_merged_data(ticker1: str, ticker2: str, start: str, end: str, dir_name: str) -> pd.DataFrame:
    # Prepare data for both tickers this also saves the data to a csv file
    ticker1_data = prepare_data(ticker1, start, end, dir_name)
    ticker2_data = prepare_data(ticker2, start, end, dir_name)
 
    # Rename the 'Close' column in each dataframe to avoid confusion after merge
    df1 = ticker1_data.rename(columns={'Close': f'close_{ticker1.lower()}'})
    df2 = ticker2_data.rename(columns={'Close': f'close_{ticker2.lower()}'})

    # Merge the dataframes on 'Date'
    merged_df = pd.merge(df1, df2, on='Date', how='inner')

    return merged_df
  
start_date="2019-10-01"
end_date="2023-12-31"

# Define the directory name
dir_name = 'data'

# Check if the directory already exists
if not os.path.exists(dir_name):
    print(f'Creating directory {dir_name}')
    # If not, create the directory
    os.makedirs(dir_name)


merged_df = get_merged_data('FOX', 'TKO', '2019-10-01', '2023-12-31', 'data')
print(merged_df)