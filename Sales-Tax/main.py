
# Name Brydnn Killpack
# Date 9/11/2024
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations

# Constants for the state and county tax rates
state_tax_rate = .05
county_tax_rate = .025

# Get the amount of the purchase.
purchase_amount = float(input("Enter purchase amount: $"))
# Calculate the state sales tax.
state_sales_tax = purchase_amount * state_tax_rate
# Calculate the county sales tax.
county_sales_tax = purchase_amount * county_tax_rate
# Calculate the total tax.
total_sales_tax = state_sales_tax + county_sales_tax
# Calculate the total of the sale.
total_sale_amount = purchase_amount + total_sales_tax
# Print information about the sale.
print(f"Purchase Amount: ${purchase_amount:.2f}")
print(f"State Sales Tax: ${state_sales_tax:.2f}")
print(f"County Sales Tax:${county_sales_tax:.2f}")
print(f"Total Sales Tax:${total_sales_tax:.2f}")
print(f"Total Sale Amount:${total_sale_amount:.2f}")
