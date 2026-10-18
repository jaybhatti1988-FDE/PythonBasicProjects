# Task 3: Create a Simple Package (shop_package)
# Inside folder shop_package/, create:

# billing.py
# Functions:
# 1. calculate_total(prices) → returns total bill (sum of all prices)
# 2. apply_tax(amount) → adds 5% tax

# Calculate sum of all prices

def calculate_total(prices):
    return sum(prices)

# Apply 5% Tax

def apply_tax(amount):
    tax=amount * 5 / 100
    return amount + tax



