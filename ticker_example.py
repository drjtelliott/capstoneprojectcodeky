import yfinance as yf

fox = yf.Ticker("FOX")

# get all stock info
fox.info

# get historical market data
hist = fox.history(period="1mo")

# show meta information about the history (requires history() to be called first)
fox.history_metadata

# show actions (dividends, splits, capital gains)
fox.actions
fox.dividends
fox.splits
fox.capital_gains  # only for mutual funds & etfs

# show share count
fox.get_shares_full(start="2022-01-01", end=None)

# show financials:
# - income statement
fox.income_stmt
fox.quarterly_income_stmt
# - balance sheet
fox.balance_sheet
fox.quarterly_balance_sheet
# - cash flow statement
fox.cashflow
fox.quarterly_cashflow
# see `Ticker.get_income_stmt()` for more options

# show holders
fox.major_holders
fox.institutional_holders
fox.mutualfund_holders

# Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default. 
# Note: If more are needed use fox.get_earnings_dates(limit=XX) with increased limit argument.
fox.earnings_dates

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
fox.isin

# show options expirations
fox.options

# show news
fox.news

# get option chain for specific expiration
opt = fox.option_chain('2024-01-19')
# data available via: opt.calls, opt.puts
