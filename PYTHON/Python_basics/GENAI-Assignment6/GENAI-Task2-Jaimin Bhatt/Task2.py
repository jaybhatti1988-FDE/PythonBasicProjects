'''
Task 2: Bill Calculator with Error Handling

Given a list of product prices:

python
prices = [120, 350, 'abc', 500, -200, 800]

Write code that:

Iterates through the list.
Tries to add only valid (positive numerical) prices to the total.
Handles:
TypeError if value is not a number
Custom exception using raise ValueError(“Negative price not allowed”)
Prints the running total.

Expected behavior: Skip invalid items but continue processing.

'''

prices = [120, 350, 'abc', 500, -200, 800]

total=0

for price in prices:

    try:

# Check is price numeric
        if not isinstance(price,(int,float)):
            raise TypeError("Price is not a number")

# Check is price negative
        if price<0:
             raise TypeError("Negative Price not allowed")


# Add Price
        total+=price

    except TypeError as error:
        print("Skipped:",price,"-",error)

    except ValueError as error:
            print("Skipped:",price,"-",error)

    else:
         print("Price added : ",price)
         print("Running Total : ",total)

print("Final Total : ",total)