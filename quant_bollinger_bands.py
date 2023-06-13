import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_bollinger_bands(stock_data, window, num_std):
    stock_data['MA'] = stock_data['Close'].rolling(window=window).mean()
    stock_data['STD'] = stock_data['Close'].rolling(window=window).std()
    stock_data['Upper'] = stock_data['MA'] + (stock_data['STD'] * num_std)
    stock_data['Lower'] = stock_data['MA'] - (stock_data['STD'] * num_std)
    return stock_data

def plot_bollinger_bands(stock_data, ticker):
    plt.figure(figsize=(14, 6))
    plt.plot(stock_data.index, stock_data['Close'], label=ticker)
    plt.plot(stock_data.index, stock_data['MA'], label='Moving Average')
    plt.plot(stock_data.index, stock_data['Upper'], label='Upper Band', linestyle='--')
    plt.plot(stock_data.index, stock_data['Lower'], label='Lower Band', linestyle='--')
    plt.legend(loc='best')
    plt.title(f'{ticker} Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.show()

def main():
    ticker = 'AAPL'
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()
    window = 20
    num_std = 2

    stock_data = get_stock_data(ticker, start_date, end_date)
    stock_data = calculate_bollinger_bands(stock_data, window, num_std)
    plot_bollinger_bands(stock_data, ticker)

if __name__ == "__main__":
    main()
