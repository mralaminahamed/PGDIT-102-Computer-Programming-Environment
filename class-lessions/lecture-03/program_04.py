# Write a program to find the largest of three numbers.

# Collect three numbers from user.
number_01 = int(input("Enter number one: "))
number_02 = int(input("Enter number two: "))
number_03 = int(input("Enter number three: "))

largest_number = ''
if number_01 > number_02:
    largest_number = number_01
else:
    largest_number = number_02

if number_03 > largest_number:
    largest_number = number_03

print("The largest number is: ", largest_number)
