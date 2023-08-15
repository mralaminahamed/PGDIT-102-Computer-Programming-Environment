n = int(input("Enter the number: "))

sums = 0

while n != 0:
    digit = n % 10
    n = n // 10
    sums += digit

print(sums)
