"""
Create an electricity bill estimator, electricity_bill.py
Inputs should be:

price per kWh in cents,
daily use in kWh, and
number of days in the billing period.

Electricity bill estimator
Enter cents per kWh: 35
Enter daily use in kWh: 4.5
Enter number of billing days: 90
Estimated bill: $141.75
"""
from prac_1.sequences import user_choice

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
electric_price = int(input("Enter cents per kWh:"))
daily_use = float(input("Enter daily use in kWh"))
billing_days = int(input("Enter number of billing days:"))
print("Electricity bill estimator  ")

while electric_price < 0 or daily_use < 0 or billing_days < 0:
    print("Invalid input")
    electric_price = int(input("Enter cents per kWh:"))
    daily_use = float(input("Enter daily use in kWh"))
    billing_days = int(input("Enter number of billing days:"))

# total cost calcu
user_TARIFF = 0
tariff_choice = int(input("Which tariff? 11 or 31:"))
if tariff_choice == 11:
    user_TARIFF = TARIFF_11
elif tariff_choice == 31:
    user_TARIFF = TARIFF_31
else:
    print("Invalid input")

total_cost = electric_price * daily_use * billing_days * user_TARIFF
print(f"the total billing is {total_cost}")
