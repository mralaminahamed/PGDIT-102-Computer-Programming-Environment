n = int(input("Enter the number: "))

oldNumber = n
newNumber = 0

while n != 0:
    digit = n % 10
    n = n // 10
    newNumber = newNumber * 10 + digit

if oldNumber == newNumber:
    print('Palindrome')
else:
    print('Not Palindrome')
