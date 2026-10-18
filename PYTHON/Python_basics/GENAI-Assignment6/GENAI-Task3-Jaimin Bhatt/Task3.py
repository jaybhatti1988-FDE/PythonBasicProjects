'''
Task 3: Custom Exception: Age Validator

1 Write a function check_age(age) that:
Raises a custom exception ValueError(“Age must be between 1 and 120”) if age is out of range.

2 In your main code:
Take age input from the user.
Use try-except to catch and print the custom error message.

'''

def check_age(age):
    if age < 1 or age > 120 :
        raise ValueError("Age must be between 1 and 120 ")
    return "Valid Age"

try:
    age = int(input("Enter age : "))
    result=check_age(age)
except ValueError as error:
    print("Error : " ,error)

else:
    print(result)
    print("Entered Age : ",age)