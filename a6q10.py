import numpy as np

# Inputs
F0 = 60         # Futures price
K = 60          # Strike price
r = 0.08        # Risk-free rate
sigma = 0.30    # Volatility
T = 0.5         # Time to maturity
n = 2           # Steps
dt = T / n      # Time per step

# Binomial parameters
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp(r * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Futures prices at terminal nodes
F_uu = F0 * u**2
F_ud = F0 * u * d
F_dd = F0 * d**2

# Option values at terminal nodes
C_uu = max(F_uu - K, 0)
C_ud = max(F_ud - K, 0)
C_dd = max(F_dd - K, 0)

# Step back to t=0.25
C_u = discount * (p * C_uu + (1 - p) * C_ud)
C_d = discount * (p * C_ud + (1 - p) * C_dd)

# Step back to t=0
C_0 = discount * (p * C_u + (1 - p) * C_d)

print(f"European Call Option Value: ${C_0:.2f}")
