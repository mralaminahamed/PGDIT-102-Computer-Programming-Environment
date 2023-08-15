# Write a program to print the reverse of a number.

# Collect a number from user.
number = int(input("Enter a number: "))

count = 0
while count <= number:
    print(number - count)
    count += 1
