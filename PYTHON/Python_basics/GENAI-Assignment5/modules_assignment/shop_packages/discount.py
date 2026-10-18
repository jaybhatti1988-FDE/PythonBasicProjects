# Task 3: Create a Simple Package (shop_package)
# Inside folder shop_package/, create:
# 
# discount.py
# Functions:
# 1. apply_discount(price, percent) → returns discounted price
# 2. flat_discount(price) → always subtracts 50 from price

# billing.py
# Functions:
# 1. calculate_total(prices) → returns total bill (sum of all prices)
# 2. apply_tax(amount) → adds 5% tax
# 
# __init__.py
# Leave it empty OR add:
# from .discount import apply_discount, flat_discount
# from .billing import calculate_total, apply_tax
# (This allows calling functions directly from the package)

# calculate Percentage discount

def apply_discount(price,percent):
    discount=(price*percent)/100
    return price-discount

# Apply flat discount of 50%

def flat_discount(price):
    return price-50