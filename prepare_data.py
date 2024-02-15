import yfinance as yf
import pandas as pd

#Capstone Project

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

def prepare_data(ticker:str, start: str, end: str): 
    print(f"Preparing data for {ticker}")

    data = download_data(ticker, start=start, end=end)
    data = clean_data(data)

    data.to_csv(f'data/{ticker.lower()}_data.csv') 

start_date="2019-10-01"
end_date="2023-12-31"

# download fox data   
prepare_data("FOX", start=start_date, end=end_date) 

# download fox data   
prepare_data("TKO", start=start_date, end=end_date)
