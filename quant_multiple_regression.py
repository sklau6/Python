import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def generate_data(n_samples):
    np.random.seed(0)
    market_returns = np.random.normal(0.05, 0.2, n_samples)
    smb_factor = np.random.normal(0.03, 0.1, n_samples)

    # Generate a stock's returns based on the market returns and SMB factor
    stock_returns = 0.6 * market_returns + 0.4 * smb_factor + np.random.normal(0, 0.1, n_samples)
    return pd.DataFrame({'Market': market_returns, 'SMB': smb_factor, 'Stock': stock_returns})

def perform_regression(data):
    X = data[['Market', 'SMB']]
    X = sm.add_constant(X)
    y = data['Stock']

    model = sm.OLS(y, X).fit()
    return model

def plot_regression(data, model):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    # Plot the stock returns vs market returns
    ax[0].scatter(data['Market'], data['Stock'], label='Data', alpha=0.5)
    ax[0].plot(data['Market'], model.params[0] + model.params[1] * data['Market'], label='Regression Line', color='r')
    ax[0].set_title('Stock Returns vs Market Returns')
    ax[0].set_xlabel('Market Returns')
    ax[0].set_ylabel('Stock Returns')
    ax[0].legend()

    # Plot the stock returns vs SMB factor
    ax[1].scatter(data['SMB'], data['Stock'], label='Data', alpha=0.5)
    ax[1].plot(data['SMB'], model.params[0] + model.params[2] * data['SMB'], label='Regression Line', color='r')
    ax[1].set_title('Stock Returns vs SMB Factor')
    ax[1].set_xlabel('SMB Factor')
    ax[1].set_ylabel('Stock Returns')
    ax[1].legend()

    plt.show()

def main():
    n_samples = 1000
    data = generate_data(n_samples)
    model = perform_regression(data)

    print(model.summary())
    plot_regression(data, model)

if __name__ == "__main__":
    main()
