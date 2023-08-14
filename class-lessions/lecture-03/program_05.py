# Write a program to find the smallest of three numbers.

# Collect three numbers from user.
number_01 = int(input("Enter number one: "))
number_02 = int(input("Enter number two: "))
number_03 = int(input("Enter number three: "))

smallest_number = ''
if number_01 < number_02:
    smallest_number = number_01
else:
    smallest_number = number_02

if number_03 < smallest_number:
    smallest_number = number_03

print("The smallest number is: ", smallest_number)
