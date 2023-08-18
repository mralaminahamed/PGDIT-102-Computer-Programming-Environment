# Write two Python function as sum() & average() to find the average of three numbers.

def sum_of_numbers(num1, num2, num3):
    return num1 + num2 + num3


def average_of_numbers(num1, num2, num3):
    total_sum = sum_of_numbers(num1, num2, num3)
    return total_sum // 3


# Collect numbers from user
number1 = int(input("Enter First Number:"))
number2 = int(input("Enter Second Number:"))
number3 = int(input("Enter Third Number:"))

# sum_result = sum_of_numbers(number1, number2, number3)
average_result = average_of_numbers(number1, number2, number3)

# print(f"The sum of {number1}, {number2}, and {number3} is: {sum_result}")
# print(f"The average of {number1}, {number2}, and {number3} is: {average_result}")
print('The average of', number1, number2, 'and', number3, 'is:', average_result)
