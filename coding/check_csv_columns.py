# filename: check_csv_columns.py
import pandas as pd

# Load the CSV just to print the column names
data = pd.read_csv('nvidia_stock_prices.csv')
print(data.columns.tolist())