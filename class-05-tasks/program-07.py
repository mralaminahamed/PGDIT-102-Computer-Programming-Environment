N = int(input('Enter number: '))
fact = 1
i = 1

while i <= N:
    fact = fact * i
    i = i + 1

print('fact = ', fact)