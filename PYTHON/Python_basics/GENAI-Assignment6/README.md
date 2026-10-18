Python Exception Handling Assignment
Overview
This assignment focuses on Python exception handling using simple and beginner-friendly programs.

The tasks demonstrate how to handle runtime errors without stopping the complete program.

Concepts Covered
try
except
Multiple except blocks
else
finally
raise
ValueError
ZeroDivisionError
TypeError
FileNotFoundError
PermissionError
Custom error messages
Task 1 - Safe Division Utility
This task accepts a numerator and denominator from the user.

It handles:

ValueError when the user enters non-numeric data.
ZeroDivisionError when the denominator is 0.
else to display the result when no error occurs.
finally to display Operation Complete.
Code
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    result = numerator / denominator

except ValueError:
    print("Invalid input. Please enter numeric values only.")

except ZeroDivisionError:
    print("Denominator cannot be zero.")

else:
    print("Division Result:", result)

finally:
    print("Operation Complete")
Example Output
Enter numerator: 100
Enter denominator: 5
Division Result: 20.0
Operation Complete
Task 2 - Bill Calculator with Error Handling
A list containing valid, invalid, and negative product prices is processed.

prices = [120, 350, "abc", 500, -200, 800]
The program:

Processes every price.
Adds positive numerical prices.
Handles TypeError for non-numeric data.
Raises ValueError for negative prices.
Skips invalid values.
Continues processing remaining values.
Displays the running total.
Code
prices = [120, 350, "abc", 500, -200, 800]

total = 0

for price in prices:

    try:
        if not isinstance(price, (int, float)):
            raise TypeError("Price is not a number")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total = total + price

    except TypeError as error:
        print("Skipped:", price, "-", error)

    except ValueError as error:
        print("Skipped:", price, "-", error)

    else:
        print("Price added:", price)
        print("Running Total:", total)

print("Final Total:", total)
Expected Output
Price added: 120
Running Total: 120
Price added: 350
Running Total: 470
Skipped: abc - Price is not a number
Price added: 500
Running Total: 970
Skipped: -200 - Negative price not allowed
Price added: 800
Running Total: 1770
Final Total: 1770
Task 3 - Custom Exception: Age Validator
This task creates a function named:

check_age(age)
The valid age range is 1 to 120.

If the age is outside this range, the program raises:

Age must be between 1 and 120
Code
def check_age(age):

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    return "Valid age"


try:
    age = int(input("Enter your age: "))

    result = check_age(age)

except ValueError as error:
    print("Error:", error)

else:
    print(result)
    print("Entered Age:", age)
Example Output
Enter your age: 30
Valid age
Entered Age: 30
For an invalid age:

Enter your age: 150
Error: Age must be between 1 and 120
Task 4 - File Reader with Exception Handling
This task asks the user for a filename and attempts to read the file.

It handles:

FileNotFoundError
PermissionError
Successful file reading
finally
When the file is successfully opened, the first three lines are displayed.

The finally block always displays:

File operation attempted.
Code
import os

# Folder where this script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))

filename = input("Enter file Name : ")
filepath = os.path.join(script_dir, filename)

try:
    file = open(filepath, 'r')
    lines = file.readlines()
    file.close()

except FileNotFoundError:
    print("File Not Found... Please check File Name properly.")

except PermissionError:
    print("Permission Denied you can't read this file.")

else:
    print("\nFirst three lines of the file : ")

    for line in lines[:3]:
        print(line.strip())

finally:
    print("File operation attempted")
Example Output
Enter file Name : sales_data.txt

First three lines of the file : 
1200
450
980
File operation attempted
If the file does not exist:

Enter the filename: wrong.txt
File not found. Please check the filename.
File operation attempted.

Task 5 - Mini Program: Safe Shopping Cart
This task creates a simple shopping cart.

The program:

Creates an empty list named cart.
Continuously asks the user to enter a product price.
Stops when the user enters q.
Converts valid input into a float.
Handles ValueError for invalid input.
Raises ValueError when the price is negative.
Adds valid prices to the shopping cart.
Displays total items and total bill.
Code
cart = []

while True:

    user_input = input("Enter product price or 'q' to quit: ")

    if user_input.lower() == "q":
        break

    try:
        price = float(user_input)

    except ValueError:
        print("Invalid input. Please enter a numericprice.")
        continue

    try:
        if price < 0:
            raise ValueError("Negative price not allowed")

    except ValueError as error:
        print("Error:", error)

    else:
        cart.append(price)
        print("Price added successfully:", price)


print("\n----- Shopping Cart Summary -----")
print("Total Items:", len(cart))
print("Total Bill:", sum(cart))
Example Output
Enter product price or 'q' to quit: 500
Price added successfully: 500.0

Enter product price or 'q' to quit: abc
Invalid input. Please enter a numeric price.

Enter product price or 'q' to quit: -200
Error: Negative price not allowed

Enter product price or 'q' to quit: 750
Price added successfully: 750.0

Enter product price or 'q' to quit: q

----- Shopping Cart Summary -----
Total Items: 2
Total Bill: 1250.0
Assignment Summary
Task	Topic	Main Exception Handling
Task 1	Safe Division	ValueError, ZeroDivisionError, else, finally
Task 2	Bill Calculator	TypeError, ValueError, raise
Task 3	Age Validator	ValueError, raise
Task 4	File Reader	FileNotFoundError, PermissionError, finally
Task 5	Shopping Cart	ValueError, raise
Learning Outcome
After completing these tasks, the following Python exception-handling concepts are demonstrated:

Handling errors using try and except
Handling different errors using multiple except blocks
Running code after successful execution using else
Running code regardless of errors using finally
Raising errors manually using raise
Handling invalid user input
Handling division-by-zero errors
Handling file-related errors
Keeping a program running after invalid data is encountered
The assignment uses simple Python logic to provide practical experience with exception handling.