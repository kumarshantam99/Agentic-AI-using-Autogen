# filename: retrieve_nvidia_stock.py
import yfinance as yf
import pandas as pd

# Define the ticker symbol for Nvidia
ticker_symbol = 'NVDA'

# Set the data period
start_date = '2024-03-23'
end_date = '2024-04-23'

# Retrieve the stock data
nvidia_data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Save the data to a CSV file
nvidia_data.to_csv('nvidia_stock_prices.csv')

# Print the data
print(nvidia_data)