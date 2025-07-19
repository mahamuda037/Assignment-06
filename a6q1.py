import numpy as np

investment_a = [225, 215, 250, 225, 205]
investment_b = [220, 225, 250, 250, 210]
r = 0.0433

# Calculate present values for each investment
def present_value(payments, rate):
    pv = 0
    for i in range(len(payments)):
        t = i + 1  # payments start at year 1
        pv += payments[i] * np.exp(-rate * t)
    return pv

pv_a = present_value(investment_a, r)
pv_b = present_value(investment_b, r)

print(f"Present Value of Investment A: {pv_a:.2f}")
print(f"Present Value of Investment B: {pv_b:.2f}")

if pv_a > pv_b:
    print("Investment A is preferable.")
else:
    print("Investment B is preferable.")