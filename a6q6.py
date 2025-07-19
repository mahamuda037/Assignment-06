import numpy as np
import matplotlib.pyplot as plt

# Option parameters
call_strike = 45
call_premium = 3
put_strike = 40
put_premium = 4
total_cost = call_premium + put_premium

# Asset prices to simulate
S = np.linspace(30, 60, 300)

# Payoffs
call_payoff = np.maximum(S - call_strike, 0)
put_payoff = np.maximum(put_strike - S, 0)
total_payoff = call_payoff + put_payoff
net_profit = total_payoff - total_cost

# Plotting
plt.figure(figsize=(10,6))
plt.plot(S, net_profit, label='Net Profit', color='blue', linewidth=2)
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.axvline(call_strike, color='red', linestyle='--', label='Call Strike ($45)')
plt.axvline(put_strike, color='green', linestyle='--', label='Put Strike ($40)')
plt.title('Long Strangle Payoff at Expiration')
plt.xlabel('Asset Price at Expiration')
plt.ylabel('Net Profit / Loss ($)')
plt.legend()
plt.grid(True)
plt.show()