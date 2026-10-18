'''
Task 5: Mini Program: Safe Shopping Cart

Create a program that:

Has a cart list → cart = []
Runs a loop asking user to enter prices.
Stops when user enters ‘q’.
Inside the loop:
Convert input to a float
Handle ValueError if user enters invalid input
Raise custom exception if price is negative
At the end, print:
Total items
Total bill
'''

cart = []

while True:

    user_input = input("Enter product price or 'q' to quit: ")

    if user_input.lower() == "q":
        break

    try:
        price = float(user_input)

    except ValueError:
        print("Invalid input. Please enter a numeric price.")
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