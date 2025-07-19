import numpy as np
from scipy.stats import norm

# Inputs
S = 30
K = 29
r = 0.05
sigma = 0.25
T = 4 / 12  # Time in years

# Black-Scholes formula components
d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)

# European Call Option Price
call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# European Put Option Price
put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Put-Call Parity Verification
parity_LHS = call_price + K * np.exp(-r * T) - S
parity_RHS = put_price

# Output
print(f"European Call Option Price: ${call_price:.2f}")
print(f"European Put Option Price: ${put_price:.2f}")
print(f"Put-Call Parity LHS: ${parity_LHS:.2f}")
print(f"Put-Call Parity RHS: ${parity_RHS:.2f}")