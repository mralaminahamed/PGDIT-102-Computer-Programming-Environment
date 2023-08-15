# Write a program to print the sum of digits in a number.

# collect a number from user.
number = input("Enter a number: ")

if number == '':
    print("The number can not be empty.")
else:
    if not number.isdigit():
        print("The number must be  digit.")
    else:
        result = 0
        for digit in number:
            result += int(digit)

        print('The result ist:', result)
