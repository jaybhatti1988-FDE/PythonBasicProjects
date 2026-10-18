Python Modules and Packages Assignment
Overview
This assignment demonstrates how to create and use Python modules and packages.

Concepts Covered
Creating Python modules
Importing complete modules
Importing specific functions
Creating Python packages
Using __init__.py
Importing package modules
Calling functions from different modules
Restrictions
No OOP
No exception handling
No file handling
Keep function logic simple
Focus only on Python modules and packages
Project Structure
modules_assignment/
│
├── main.py
├── math_utils.py
├── string_utils.py
│
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py
Task 1 - Create a Simple Module
Create a module named math_utils.py.

It contains three functions:

add(a, b) - returns addition of two numbers
subtract(a, b) - returns subtraction of two numbers
square(n) - returns square of a number
math_utils.py
# Add two numbers
def add(a, b):
    return a + b


# Subtract two numbers
def subtract(a, b):
    return a - b


# Calculate square
def square(n):
    return n ** 2
In main.py, the module is imported in two ways:

import math_utils

from math_utils import square
Example:

print("----- Math Utils -----")

print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(5))
Task 2 - Create Another Module
Create another module named string_utils.py.

It contains three functions:

capitalize_words(text) - capitalizes each word
reverse_string(text) - reverses the text
word_count(text) - counts the total number of words
string_utils.py
# Capitalize each word
def capitalize_words(text):
    return text.title()


# Reverse string
def reverse_string(text):
    return text[::-1]


# Count words
def word_count(text):
    return len(text.split())
Import the module in main.py:

import string_utils
Example:

print("\n----- String Utils -----")

text = "python module assignment"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))
Task 3 - Create a Simple Package
Create a package named:

shop_package
The package contains:

shop_package/
├── __init__.py
├── discount.py
└── billing.py
discount.py
Create two discount-related functions.

# Apply percentage discount
def apply_discount(price, percent):
    discount = (price * percent) / 100
    return price - discount


# Apply flat discount of 50
def flat_discount(price):
    return price - 50
Example
For:

apply_discount(1000, 10)
The result is:

900.0
For:

flat_discount(1000)
The result is:

950
billing.py
Create two billing-related functions.

# Calculate total bill
def calculate_total(prices):
    return sum(prices)


# Add 5% tax
def apply_tax(amount):
    tax = amount * 5 / 100
    return amount + tax
Example:

calculate_total([100, 200, 300])
Result:

600
For a total amount of 600, applying 5% tax gives:

630.0
init.py
The __init__.py file makes shop_package a Python package.

Add:

from .discount import apply_discount, flat_discount
from .billing import calculate_total, apply_tax
Task 4 - Import the Package in main.py
Import the package using:

import shop_package.discount as disc

from shop_package.billing import calculate_total
from shop_package.billing import apply_tax
Test all package functions.

print("\n----- Shop Package -----")

# Test percentage discount
print("Discounted Price:", disc.apply_discount(1000, 10))

# Test flat discount
print("Flat Discount:", disc.flat_discount(1000))

# Test total bill
prices = [100, 200, 300]

total = calculate_total(prices)

print("Total Bill:", total)

# Test tax
print("Total After Tax:", apply_tax(total))
Complete main.py
The final main.py combines Tasks 1, 2, and 4.

# ==================================
# Task 1 - Math Utils
# ==================================

import math_utils
from math_utils import square


print("----- Math Utils -----")

print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(5))


# ==================================
# Task 2 - String Utils
# ==================================

import string_utils


print("\n----- String Utils -----")

text = "python module assignment"

print("Capitalized:", string_utils.capitalize_words(text))
print("Reversed:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# ==================================
# Task 4 - Shop Package
# ==================================

import shop_package.discount as disc

from shop_package.billing import calculate_total
from shop_package.billing import apply_tax


print("\n----- Shop Package -----")

# Percentage Discount
print("Discounted Price:", disc.apply_discount(1000, 10))

# Flat Discount
print("Flat Discount:", disc.flat_discount(1000))

# Calculate Total
prices = [100, 200, 300]

total = calculate_total(prices)

print("Total Bill:", total)

# Apply Tax
print("Total After Tax:", apply_tax(total))
Expected Output
----- Math Utils -----
Addition: 15
Subtraction: 5
Square: 25

----- String Utils -----
Capitalized: Python Module Assignment
Reversed: tnemngissa eludom nohtyp
Word Count: 3

----- Shop Package -----
Discounted Price: 900.0
Flat Discount: 950
Total Bill: 600
Total After Tax: 630.0
How to Run
Open the terminal inside the modules_assignment folder.

Run:

python main.py
Summary
Task 1
Created math_utils.py with addition, subtraction, and square functions.

Task 2
Created string_utils.py with capitalize, reverse, and word-count functions.

Task 3
Created shop_package containing discount and billing modules with an __init__.py file.

Task 4
Imported the modules and package functions into main.py and tested all functions.

This assignment demonstrates the basic use of Python modules, imports, functions, and packages in a simple beginner-friendly project.