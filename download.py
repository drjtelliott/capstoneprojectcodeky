import yfinance as yf
import pandas as pd

# reference for download: https://github.com/ranaroussi/yfinance/wiki/Tickers#download

def download_data(ticker:str, start: str, end: str) -> pd.DataFrame: 
    print("Downloading {ticker} data....")

    # using yfinance download ticker information for particular date range
    data = yf.download(ticker, start=start, end=end)

    # update data frame to only contain column we care about
    data = data.drop(columns=['Open', 'High', 'Low', 'Adj Close'])

    print("...{ticker} data downloaded")

    # return the pandas dataframe
    return data

# download fox data   
fox_data = download_data("FOX", start="2023-01-01", end="2023-12-22")
fox_data.to_csv('data/fox_data.csv', index=False) 

# download fox data   
tko_data = download_data("TKO", start="2023-01-01", end="2023-12-22")
tko_data.to_csv('data/tko_data.csv', index=False) 
