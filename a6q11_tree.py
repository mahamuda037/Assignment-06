import numpy as np
import matplotlib.pyplot as plt

# Parameters
S0 = 484
K = 480
r = 0.10
q = 0.03
sigma = 0.25
T = 2 / 12
N = 4
dt = T / N

# Binomial factors
u = np.exp(sigma * np.sqrt(dt))
d = 1 / u
p = (np.exp((r - q) * dt) - d) / (u - d)
discount = np.exp(-r * dt)

# Initialize trees
stock_tree = np.zeros((N+1, N+1))
option_tree = np.zeros((N+1, N+1))

# Fill stock price tree
for j in range(N+1):
    for i in range(j+1):
        stock_tree[i, j] = S0 * (u**(j - i)) * (d**i)

# Terminal payoffs for American put
for i in range(N+1):
    option_tree[i, N] = max(K - stock_tree[i, N], 0)

# Backward induction
for j in reversed(range(N)):
    for i in range(j+1):
        hold = discount * (p * option_tree[i, j+1] + (1 - p) * option_tree[i+1, j+1])
        exercise = K - stock_tree[i, j]
        option_tree[i, j] = max(hold, exercise)

# Plotting function
def plot_tree(tree, title):
    plt.figure(figsize=(10, 6))
    for j in range(N+1):
        for i in range(j+1):
            x = j
            y = -i  # invert y to show upward movement in tree
            value = tree[i, j]
            plt.scatter(x, y, color='skyblue')
            plt.text(x, y, f'{value:.2f}', ha='center', va='center', fontsize=9, fontweight='bold')

    plt.title(title)
    plt.xticks(range(N+1))
    plt.yticks([])
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel('Time Step')
    plt.ylabel('Tree Levels')
    plt.tight_layout()
    plt.show()

# Show the trees
plot_tree(stock_tree, 'Stock Price Binomial Tree')
plot_tree(option_tree, 'American Put Option Value Tree')