import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from ta import add_all_ta_features
from ta.utils import dropna

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def add_technical_indicators(stock_data):
    stock_data = dropna(stock_data)
    stock_data = add_all_ta_features(stock_data, open="Open", high="High", low="Low", close="Close", volume="Volume")
    return stock_data

def plot_rsi_macd(stock_data, ticker):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

    ax1.plot(stock_data.index, stock_data['Close'], label=ticker)
    ax1.set_title(f'{ticker} Price History')
    ax1.set_ylabel('Price')

    ax2.plot(stock_data.index, stock_data['momentum_rsi'], label='RSI', color='g')
    ax2.axhline(30, linestyle='--', color='r')
    ax2.axhline(70, linestyle='--', color='r')
    ax2.set_title('Relative Strength Index (RSI)')
    ax2.set_ylabel('RSI')

    ax3.plot(stock_data.index, stock_data['trend_macd'], label='MACD', color='b')
    ax3.plot(stock_data.index, stock_data['trend_macd_signal'], label='Signal Line', color='g')
    ax3.set_title('Moving Average Convergence Divergence (MACD)')
    ax3.set_xlabel('Date')
    ax3.set_ylabel('MACD')
    ax3.legend(loc='best')

    plt.tight_layout()
    plt.show()

def main():
    ticker = 'AAPL'
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()

    stock_data = get_stock_data(ticker, start_date, end_date)
    stock_data = add_technical_indicators(stock_data)
    plot_rsi_macd(stock_data, ticker)

if __name__ == "__main__":
    main()
