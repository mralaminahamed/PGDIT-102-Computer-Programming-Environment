# Write a program to calculate the factorial of a given number.

# Fibonacci series
# in mathematics, the product of all positive integers less than or equal to a given
# positive integer and denoted by that integer and an exclamation point. Thus, factorial seven is written 7!,
# meaning 1 × 2 × 3 × 4 × 5 × 6 × 7.

N = int(input('Enter number: '))
fact = 1
i = 1

while i <= N:
    fact *= i
    i += 1

print('fact = ', fact)
