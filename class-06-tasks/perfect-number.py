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
