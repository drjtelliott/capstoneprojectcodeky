import yfinance as yf

# reference for download: https://github.com/ranaroussi/yfinance/wiki/Tickers#download

def download_data(ticker:str, start: str, end: str) -> any: 
    # using yfinance download ticker information for particular date range
    data = yf.download(ticker, start=start, end=end)

    # update data frame to only contain column we care about
    data = data.drop(columns=['Open', 'High', 'Low', 'Adj Close'])

    # return the pandas dataframe
    return data

# download fox data  
print("FOX DATA") 
fox_data = download_data("FOX", start="2023-01-01", end="2023-12-22")
print(fox_data)

# download fox data  
print("TKO DATA") 
tko_data = download_data("TKO", start="2023-01-01", end="2023-12-22")
print(tko_data)
