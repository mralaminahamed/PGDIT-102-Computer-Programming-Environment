def find_max_of_three_numbers(num1, num2, num3):
    # Compare num1 and num2 to find the maximum of the first two numbers
    if num1 > num2:
        max_number = num1
    else:
        max_number = num2

    # Compare the maximum of the first two numbers with the third number
    if max_number < num3:
        max_number = num3

    return max_number


# Collect any three numbers from end user.
first_number = int(input("Enter the first numbers: "))
second_number = int(input("Enter the second numbers: "))
third_number = int(input("Enter the third numbers: "))

# Show the max number to the screen
print("The max number is: ", find_max_of_three_numbers(first_number, second_number, third_number))
