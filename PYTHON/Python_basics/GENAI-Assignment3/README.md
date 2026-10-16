# Python Functions Assignment

## Overview

This project demonstrates basic and recursive functions in Python. It includes a discount calculator and a factorial utility.

## Task 1: Price After Discount

The `apply_discount(price, discount_percent=5)` function calculates and returns the final price after applying a discount. If the discount percentage is not provided, the function applies a default discount of 5%. The optional validation ensures that the discount does not exceed 60%.

### Tests

```python
print(apply_discount(1000, 10))
print(apply_discount(500))
```

## Task 2: Recursive Factorial Utility

The `factorial(n)` function calculates the factorial of a number using recursion. It returns `1` when `n` is `0` or `1`. If a negative value is provided, the function displays an error message.

### Tests

```python
print(factorial(5))
print(factorial(0))
print(factorial(-3))
```


## Task 3: GST Calculator

Create a lambda function that adds 18% GST to a price.

```python
gst = lambda price: price + (0.18 * price)
print(gst(100))  # 118.0
```

Optional: Create another lambda function to calculate the final price after applying both GST and discount.

## Task 4: Apply GST Using map()

Use `map()` with the GST lambda to calculate GST-inclusive prices.

```python
prices = [100, 250, 400, 1200, 50]
prices_with_gst = list(map(gst, prices))

print("Original prices:", prices)
print("Prices after GST:", prices_with_gst)
```

## Task 5: Filter Product Prices

Use `filter()` to separate prices greater than 500 and prices less than or equal to 500.

```python
prices = [100, 250, 400, 1200, 50, 2000, 850]

expensive_prices = list(filter(lambda price: price > 500, prices))
affordable_prices = list(filter(lambda price: price <= 500, prices))

print("Prices greater than 500:", expensive_prices)
print("Prices less than or equal to 500:", affordable_prices)
```

## Task 6: Combined Utility Function

The `process_prices(prices)` function accepts a list of prices. It uses `map()` with a lambda expression to apply a 10% discount to every price. It then uses `filter()` to keep only discounted prices greater than 300.

The function returns two lists:

- `discounted_prices`
- `filtered_prices`

### Test

```python
process_prices([100, 500, 900, 50, 750])
```

## Task 7: Menu Using Functions

Task 7 creates three reusable functions:

- `add_price(prices_list, price)` adds a price to the list.
- `get_average_price(prices_list)` returns the average price.
- `get_max_price(prices_list)` returns the highest price.

### Menu Options

- `1` - Add price
- `2` - Show average price
- `3` - Show highest price
- `q` - Quit

The menu uses a loop and function calls only. Object-oriented programming is not required.

## Concepts Used

- Lambda functions
- `map()`
- `filter()`
- Lists
- Basic arithmetic
- Conditional expressions
- Function definition
- Function parameters
- Default arguments
- Return statements
- Conditional statements
- Recursion
- Input validation
- Functions and return values
- Lambda expressions
- Lists and loops
- Conditional statements
- Menu-driven programming
