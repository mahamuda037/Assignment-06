import numpy as np
import matplotlib.pyplot as plt

F0 = 60           # Current futures price
K = 60            # Strike price
r = 0.08          # Risk-free interest rate
sigma = 0.30      # Volatility
T = 0.5           # Time to maturity (in years)
N = 2             # Number of steps
dt = T / N        # Time per step

# Binomial model parameters
u = np.exp(sigma * np.sqrt(dt))           # Up factor
d = 1 / u                                  # Down factor
p = (np.exp(r * dt) - d) / (u - d)         # Risk-neutral probability

# Step 1: Build the futures price tree
F = [[0 for _ in range(i + 1)] for i in range(N + 1)]
for i in range(N + 1):
    for j in range(i + 1):
        F[i][j] = F0 * (u ** j) * (d ** (i - j))

# Step 2: Calculate option value at maturity    
C = [[0 for _ in range(i + 1)] for i in range(N + 1)]
for j in range(N + 1):
    C[N][j] = max(F[N][j] - K, 0)  # C_N = max(F_N - K, 0)

# Step 3: Backward induction for option value
for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        C[i][j] = np.exp(-r*T) * (p * C[i + 1][j + 1] + (1 - p) * C[i + 1][j])

# Step 4: Print trees
print("Futures Price Tree:")
for row in F:
    print([f'{val:.2f}'for val in row])

print("\nEuropean Call Option Tree:")
for row in C:
    print([f'{val:.2f}'for val in row])

print(f"\nEuropean Call Option Value: {C[0][0]:.4f}")

# Step 5: Plotting function for both futures and option tree
def plot_combined_tree(F, C, title):
    fig, ax = plt.subplots(figsize=(8, 6))

    for i in range(len(F)):
        for j in range(len(F[i])):
            x = i
            y = -j + i / 2  # Diagonal layout

            futures = F[i][j]
            option = C[i][j]

            label = f"F: {futures:.2f}\nC: {option:.2f}"
            ax.text(x, y, label, fontsize=11,
                    bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.3'),
                    ha='center')

            # Draw arrows to next nodes
            if i < len(F) - 1:
                ax.plot([x, x + 1], [y, y - 0.5], color='gray', linestyle='--')  # down
                ax.plot([x, x + 1], [y, y + 0.5], color='gray', linestyle='--')  # up

    ax.set_title(title, fontsize=14)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

# Step 6: Plot combined tree
plot_combined_tree(F, C, "Futures and European Call Option Price Tree")


# Step 7: American Call Option Tree
A = [[0 for _ in range(i + 1)] for i in range(N + 1)]

# Terminal payoffs same as European
for j in range(N + 1):
    A[N][j] = max(F[N][j] - K, 0)

# Backward induction allowing early exercise
early_exercise_flag = False
for i in range(N - 1, -1, -1):
    for j in range(i + 1):
        hold = np.exp(-r*T) * (p * A[i + 1][j + 1] + (1 - p) * A[i + 1][j])
        exercise = F[i][j] - K
        A[i][j] = max(hold, exercise)

        # Check if early exercise is optimal at any node
        if exercise > hold:
            early_exercise_flag = True

print("\nAmerican Call Option Tree:")
for row in A:
    print([f"{val:.2f}"for val in row])

print(f"\nAmerican Call Option Value: {A[0][0]:.4f}")
if early_exercise_flag:
    print("\nYES, it is optimal to exercise early at some nodes.")
else:
    print("\nNO, early exercise is never optimal — matches European option.")

plot_combined_tree(F, A, "Futures and American Call Option Price Tree")