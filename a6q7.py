import math

# Given parameters
C = 1              # Call option price
K = 20             # Strike price
r = 0.03           # Risk-free rate (annual)
T = 4 / 12         # Time to expiration in years (4 months)
S = 19             # Current stock price

# Put-Call Parity formula: P = C + K * e^(-rT) - S
discounted_strike = K * math.exp(-r * T)
put_price = C + discounted_strike - S

print(f"European Put Option Price: ${put_price:.2f}")