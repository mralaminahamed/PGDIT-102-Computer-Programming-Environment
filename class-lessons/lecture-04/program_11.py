# Write a program to display Fibonacci series up to 10 terms.

# Fibonacci series
# an infinite series, starting from '0' and '1', in which every number in the series is the
# sum of two numbers preceding it in the series. Fibonacci series numbers are, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
# 89 , 144, .......


# Collect the terms from user.
term = int(input('Enter the number:'))

# Assign required variables.
first = 0
second = 1
i = 2

# print(first, second, count)

while i < term:
    newNumber = first + second

    # show new number.
    print(newNumber)

    # Update the count numbers.
    i += 1

    # Update first and second numbers.
    first = second
    second = newNumber
