# Question: Write a program to check whether a given number is even or odd.

# Collect a number from user.
number = int(input("Enter a number: "))

# Check whether the given number is event or odd.
# even = জোড়
# odd = বিজোড়
if number % 2:  # the output will be 1 for every odd number
    print("The number is odd")
else:
    print("The number is even")
