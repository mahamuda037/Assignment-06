import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Black-Scholes pricing for European options
def black_scholes(option_type, S, K, r, T, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    else:
        return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Constants
S0 = 32
sigma = 0.30
r = 0.05

# Range of final stock prices
S_range = np.linspace(10, 55, 200)

# Strategy setup
def payoff(strategy_name):
    if strategy_name == 'bull_call':
        T = 0.5
        K1, K2 = 25, 30
        C1 = black_scholes('call', S0, K1, r, T, sigma)
        C2 = black_scholes('call', S0, K2, r, T, sigma)
        cost = C1 - C2
        return np.maximum(S_range - K1, 0) - np.maximum(S_range - K2, 0) - cost

    elif strategy_name == 'bear_put':
        T = 0.5
        K1, K2 = 25, 30
        P1 = black_scholes('put', S0, K1, r, T, sigma)
        P2 = black_scholes('put', S0, K2, r, T, sigma)
        cost = P2 - P1
        return np.maximum(K2 - S_range, 0) - np.maximum(K1 - S_range, 0) - cost

    elif strategy_name == 'butterfly_call':
        T = 1.0
        K1, K2, K3 = 25, 30, 35
        C1 = black_scholes('call', S0, K1, r, T, sigma)
        C2 = black_scholes('call', S0, K2, r, T, sigma)
        C3 = black_scholes('call', S0, K3, r, T, sigma)
        cost = C1 + C3 - 2*C2
        return np.maximum(S_range - K1, 0) + np.maximum(S_range - K3, 0) - 2*np.maximum(S_range - K2, 0) - cost

    elif strategy_name == 'butterfly_put':
        T = 1.0
        K1, K2, K3 = 25, 30, 35
        P1 = black_scholes('put', S0, K1, r, T, sigma)
        P2 = black_scholes('put', S0, K2, r, T, sigma)
        P3 = black_scholes('put', S0, K3, r, T, sigma)
        cost = P1 + P3 - 2*P2
        return np.maximum(K1 - S_range, 0) + np.maximum(K3 - S_range, 0) - 2*np.maximum(K2 - S_range, 0) - cost

    elif strategy_name == 'straddle':
        T = 0.5
        K = 30
        C = black_scholes('call', S0, K, r, T, sigma)
        P = black_scholes('put', S0, K, r, T, sigma)
        cost = C + P
        return np.maximum(S_range - K, 0) + np.maximum(K - S_range, 0) - cost

    elif strategy_name == 'strangle':
        T = 0.5
        K1, K2 = 25, 35
        C = black_scholes('call', S0, K2, r, T, sigma)
        P = black_scholes('put', S0, K1, r, T, sigma)
        cost = C + P
        return np.maximum(S_range - K2, 0) + np.maximum(K1 - S_range, 0) - cost

# Plotting all strategies
strategies = ['bull_call', 'bear_put', 'butterfly_call', 'butterfly_put', 'straddle', 'strangle']
titles = ['Bull Spread (Call)', 'Bear Spread (Put)', 'Butterfly Spread (Call)',
          'Butterfly Spread (Put)', 'Straddle', 'Strangle']

plt.figure(figsize=(16, 10))
for i, strat in enumerate(strategies):
    plt.subplot(2, 3, i+1)
    profit = payoff(strat)
    plt.plot(S_range, profit, label='Profit', color='blue')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.title(titles[i])
    plt.xlabel('Final Stock Price')
    plt.ylabel('Profit ($)')
    plt.grid(True)

plt.tight_layout()
plt.show()