import numpy as np

S0 = 40           # Initial stock price
r = 0.10          # Continuously compounded annual interest rate
T = 1             # Time to maturity in years
St = 45           # Stock price at t = 0.5 years
t = 0.5           # Time passed

# (a) Forward price and value at t = 0
F0 = S0 * np.exp(r * T)
V0 = 0  # Initial value of the forward contract

# (b) Forward price and value at t = 0.5
Ft = St * np.exp(r * (T - t))
Vt = St - F0 * np.exp(-r * (T - t))

# Output
print(f"(a) At inception:")
print(f"Forward Price F0 = ${F0:.2f}")
print(f"Initial Value V0 = ${V0:.2f}")

print(f"\n(b) Six months later:")
print(f"Forward Price Ft = ${Ft:.2f}")
print(f"Value of Original Contract Vt = ${Vt:.2f}")