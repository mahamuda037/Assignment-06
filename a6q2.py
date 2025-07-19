import numpy as np

# Parameters
face_value = 100
coupon_rate = 0.08
coupon = face_value * coupon_rate #cash flow
years = 5
yield_initial = 0.11  # Initial continuously compounded yield
yield_new = 0.108     # After 0.2% decrease
delta_yield = yield_new - yield_initial

# --- Price Function ---
def bond_price(coupon, face_value, r, T):
    pv_coupons = sum([coupon * np.exp(-r * t) for t in range(1, T + 1)])
    pv_face = face_value * np.exp(-r * T)
    return pv_coupons + pv_face

# --- Duration Function ---
def bond_duration(coupon, face_value, r, T, price):
    weighted_sum = sum([t * coupon * np.exp(-r * t) for t in range(1, T + 1)])
    weighted_sum += T * face_value * np.exp(-r * T)
    return weighted_sum / price

# --- Calculations ---
price_initial = bond_price(coupon, face_value, yield_initial, years)
duration = bond_duration(coupon, face_value, yield_initial, years, price_initial)

# Price change estimation via duration
price_change = -duration * price_initial * delta_yield
price_estimated = price_initial + price_change

# Exact new price at 10.8% yield
price_new_exact = bond_price(coupon, face_value, yield_new, years)

# --- Output ---
print(f"Initial Bond Price (11% yield): ${price_initial:.2f}")
print(f"Duration: {duration:.2f} years")
print(f"Estimated Price after 0.2% yield drop: ${price_estimated:.2f}")
print(f"Exact Price at 10.8% yield: ${price_new_exact:.2f}")