import datetime
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

def calculate_log_returns(stock_data):
    stock_data['LogReturns'] = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
    return stock_data

def monte_carlo_simulation(stock_data, num_simulations, num_days):
    last_price = stock_data['Close'].iloc[-1]
    log_returns = stock_data['LogReturns']

    simulations = np.zeros((num_simulations, num_days))
    for i in range(num_simulations):
        daily_returns = np.random.normal(log_returns.mean(), log_returns.std(), num_days)
        simulations[i] = last_price * np.exp(np.cumsum(daily_returns))

    return simulations

def plot_monte_carlo(simulations, ticker):
    plt.figure(figsize=(14, 6))
    plt.plot(simulations)
    plt.title(f'{ticker} Monte Carlo Simulation')
    plt.xlabel('Days')
    plt.ylabel('Price')
    plt.show()

def main():
    ticker = 'AAPL'
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime.now()
    num_simulations = 1000
    num_days = 252

    stock_data = get_stock_data(ticker, start_date, end_date)
    stock_data = calculate_log_returns(stock_data)
    simulations = monte_carlo_simulation(stock_data, num_simulations, num_days)
    plot_monte_carlo(simulations, ticker)

if __name__ == "__main__":
    main()
