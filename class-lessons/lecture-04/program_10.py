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

        print('The result is:', result)


# n = int(input("Enter the number: "))
#
# sums = 0
#
# while n != 0:
#     digit = n % 10
#     n = n // 10
#     sums += digit
#
# print(sums)