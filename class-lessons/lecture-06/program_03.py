# Write a Python function to sum all the numbers in a list.

def sum_of_numbers(numbers_list):
    total_sum = 0

    for num in numbers_list:
        total_sum += num

    return total_sum


if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    result = sum_of_numbers(numbers)
    print(f"The sum of the numbers in the list is: {result}")
