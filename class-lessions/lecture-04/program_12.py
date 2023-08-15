# Write a program to check whether a given number is a 'Perfect' number or
# not. Perfect number, a positive integer that is equal to the sum of its
# proper divisors. The smallest perfect number is 6, which is the sum of 1, 2,
# and 3.

# Collect the number from user.
number = int(input('Enter the number:'))

# Assign required variables.
sums = 0

# check the factors.
for i in range(1, number):
    if (number % i) == 0:
        sums += i

if sums == number:
    print(number, 'is a perfect number')
else:
    print(number, 'is not a perfect number')
