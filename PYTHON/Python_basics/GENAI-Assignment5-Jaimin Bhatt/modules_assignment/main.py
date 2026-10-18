## TASK 1 Create a Simple Module (math_utils.py)

import math_utils
from math_utils import square

print("------------ Math Utils ------------")

# Test Add
print("Addition:",math_utils.add(10,5))

# Test Sub
print("Subtraction:",math_utils.sub(10,5))

# Test Square
print("Square:",math_utils.square(10))

# Task 2: Create Another Module (string_utils.py)

import string_utils

print("\n-------------- String Utils --------------")
text="python Module assignment"

# Test capitalize each word 
print("Capitalized:",string_utils.capitalize_words(text))

# Test reversed string
print("Reversed:",string_utils.reverse_string(text))

# Test number of words count in the text 
print("Word Count:",string_utils.word_count(text))


# Task 4: Importing the Package in main.py 
# 
# In main.py, do the following:
# 1. import shop_package.discount as disc
# 2. from shop_package.billing import calculate_total
# 3. Call every function inside the package.

import shop_packages.discount as disc
from shop_packages.billing import calculate_total
from shop_packages.billing import apply_tax

print("\n---------- Shop Packages ------------")

# Test apply Discount()
print("Discount Price",disc.apply_discount(1000,10))

# Test apply Flat Discount()
print("Flat Discount",disc.flat_discount(1000))

# Test Calculate total()

prices=[100,200,300]
total=calculate_total(prices)
print("Total Bill:",total)

# Test apply Tax()

print("Total After Tax:",apply_tax(total))