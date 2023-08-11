# Write a Python program to print the even numbers from a given list.

def print_even_numbers(numbers_list):
    print("Even numbers in the list:")

    for num in numbers_list:
        if num % 2 == 0:
            print(num)


def print_odd_numbers(numbers_list):
    print("Even numbers in the list:")

    for num in numbers_list:
        if num % 2 != 0:
            print(num)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_even_numbers(numbers)
