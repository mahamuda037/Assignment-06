#PV=FV/(1+r/n)^(n*t) #FV=future value,PV=present Value, n=4
# Cash flows for year 1 to 6
cash_flows = [460, 235, 640, 370, 330, 250]
annual_rate = 4.5 / 100
# Quarterly compounding
n = 4  # compounding periods per year

# Calculate Present Value for each year
def calculate_present_value(FV, year, rate, n):
    t = year
    return FV / (1 + rate/n) ** (n * t)

# Total PV calculation
total_pv = 0
for year, payment in enumerate(cash_flows, start=1):
    pv = calculate_present_value(payment, year, annual_rate, n)
    total_pv += pv
    print(f"Year {year}: Future Value = {payment}, Present Value = {pv:.2f}")

print(f"\nTotal Present Value of all payments: {total_pv:.2f} taka")