import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_moving_averages(stock_data, short_window, long_window):
    stock_data['ShortMA'] = stock_data['Close'].rolling(window=short_window).mean()
    stock_data['LongMA'] = stock_data['Close'].rolling(window=long_window).mean()
    return stock_data

def backtest_strategy(stock_data, short_window):
    stock_data['Signal'] = 0.0
    stock_data['Signal'][short_window:] = np.where(
        stock_data['ShortMA'][short_window:] > stock_data['LongMA'][short_window:], 1.0, 0.0
    )
    stock_data['Position'] = stock_data['Signal'].diff()
    return stock_data

def plot_strategy(stock_data, ticker):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    ax1.plot(stock_data.index, stock_data['Close'], label='Price', alpha=0.5)
    ax1.plot(stock_data.index, stock_data['ShortMA'], label='Short MA', linestyle='--', color='g')
    ax1.plot(stock_data.index, stock_data['LongMA'], label='Long MA', linestyle='--', color='r')
    ax1.set_title(f'{ticker} Moving Average Crossover Strategy')
    ax1.set_ylabel('Price')
    ax1.legend(loc='best')

    ax2.plot(stock_data.index, stock_data['Signal'], label='Signal', linestyle='--', color='b')
    ax2.plot(stock_data.index, stock_data['Position'], label='Position', linestyle='-', color='k')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Signal')
    ax2.legend(loc='best')

    plt.tight_layout()
    plt.show()

def main():
    ticker = 'AAPL'
    start_date = datetime.datetime(2018, 1, 1)
    end_date = datetime.datetime.now()
    short_window = 50
    long_window = 200

    stock_data = get_stock_data(ticker, start_date, end_date)
    stock_data = calculate_moving_averages(stock_data, short_window, long_window)
    stock_data = backtest_strategy(stock_data, short_window)
    plot_strategy(stock_data, ticker)

if __name__ == "__main__":
    main()
