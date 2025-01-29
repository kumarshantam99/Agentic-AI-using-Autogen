# filename: revised_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file specifying the first column as the index
data = pd.read_csv('nvidia_stock_prices.csv', index_col=0, parse_dates=True)

# Calculate maximum, minimum, and average closing price
max_close_price = data['Close'].max()
min_close_price = data['Close'].min()
average_close_price = data['Close'].mean()

# Identifying the biggest drop
data['Previous_Close'] = data['Close'].shift(1)
data['Price_Change'] = data['Close'] - data['Previous_Close']
largest_drop = data['Price_Change'].min()

# Prepare summary of findings
print(f"Maximum Close Price: {max_close_price}")
print(f"Minimum Close Price: {min_close_price}")
print(f"Average Close Price: {average_close_price}")
print(f"Largest Single Day Drop: {largest_drop}")

# Plot the closing prices
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label='Closing Price')
plt.title('Nvidia Stock Closing Prices from March 23, 2024 to April 23, 2024')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()