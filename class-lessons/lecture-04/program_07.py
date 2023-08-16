# Write a program to calculate the factorial of a given number.

# factorial,
# in mathematics, the product of all positive integers less than or equal to a given
# positive integer and denoted by that integer and an exclamation point. Thus, factorial seven is written 7!,
# meaning 1 × 2 × 3 × 4 × 5 × 6 × 7.

N = int(input('Enter number: '))
result = 1
index = 1

while index <= N:
    # result = result * index
    result *= index
    index += 1

print('fact = ', result)
