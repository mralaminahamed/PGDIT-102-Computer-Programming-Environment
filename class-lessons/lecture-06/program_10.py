# Write a program in Python to find the GCD of two numbers using recursion.

def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


# Collect numbers from user
number1 = int(input("Enter First Number:"))
number2 = int(input("Enter Second Number:"))

# Calculate the GCD of numbers
result = gcd_recursive(number1, number2)
print(f"The GCD of {number1} and {number2} is: {result}")

