n = int(input("Enter the number: "))

newNumber = 0

while n != 0:
    digit = n % 10
    n = n // 10
    newNumber = newNumber * 10 + digit

print(newNumber)
