import numpy as np
import matplotlib.pyplot as plt

K = 150
premium = 5
S = np.linspace(0, 300, 100)

# --- Option calculations ---
# Long Call
payoff_long_call = np.maximum(S - K, 0)
profit_long_call = payoff_long_call - premium

# Short Call
payoff_short_call = -np.maximum(S - K, 0)
profit_short_call = payoff_short_call + premium

# Long Put
payoff_long_put = np.maximum(K - S, 0)
profit_long_put = payoff_long_put - premium

# Short Put
payoff_short_put = -np.maximum(K - S, 0)
profit_short_put = payoff_short_put + premium

# --- Plotting ---
plt.figure(figsize=(12, 10))

# Long Call Plot
plt.subplot(2, 2, 1)
plt.plot(S, payoff_long_call, label='Payoff', linestyle='--')
plt.plot(S, profit_long_call, label='Profit')
plt.title('Long Call Option')
plt.xlabel('Stock Price')
plt.ylabel('Payoff / Profit')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Short Call Plot
plt.subplot(2, 2, 2)
plt.plot(S, payoff_short_call, label='Payoff', linestyle='--')
plt.plot(S, profit_short_call, label='Profit')
plt.title('Short Call Option')
plt.xlabel('Stock Price')
plt.ylabel('Payoff / Profit')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Long Put Plot
plt.subplot(2, 2, 3)
plt.plot(S, payoff_long_put, label='Payoff', linestyle='--')
plt.plot(S, profit_long_put, label='Profit')
plt.title('Long Put Option')
plt.xlabel('Stock Price')
plt.ylabel('Payoff / Profit')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

# Short Put Plot
plt.subplot(2, 2, 4)
plt.plot(S, payoff_short_put, label='Payoff', linestyle='--')
plt.plot(S, profit_short_put, label='Profit')
plt.title('Short Put Option')
plt.xlabel('Stock Price')
plt.ylabel('Payoff / Profit')
plt.axhline(0, color='black', linewidth=0.5)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()