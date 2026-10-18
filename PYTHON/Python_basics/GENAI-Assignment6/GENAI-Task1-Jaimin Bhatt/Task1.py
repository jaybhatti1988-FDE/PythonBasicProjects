'''
Task 1: Safe Division Utility

 Write a program that:

Takes two inputs from the user: numerator and denominator.
Uses try-except to handle:
ValueError (if input is not a number)
ZeroDivisionError (if denominator = 0)
If no error occurs, print the result inside the else block.
In the finally block, print:

“Operation Complete” 
'''

# Safe Division Utility

try:
    numerator=float(input("Enter Numerator : "))
    denominator=float(input("Enter Denominator : "))

    result=numerator/denominator

except ValueError:
    print("Invalid Input. Please enter valid numeric value")

except ZeroDivisionError:
    print("Denominator can't be Zero")

else:
    print("Division Result :",result)        

finally:
    print("Operation Completed")