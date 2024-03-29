# Write a Python function to calculate the factorial of a number using recursive
# function.

def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
        return n * factorial_recursive(n - 1)


# Collect numbers from user
num = int(input("Enter Number:"))

if num < 0:
    print("Sorry, this number is less than zero. Please enter greater than 0.")
else:
    result = factorial_recursive(num)
    print(f"The factorial of {num} is: {result}")
