# Write a program in Python to calculate the sum of numbers from 1 to n using
# recursion.

def sum_numbers_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers_recursive(n - 1)


if __name__ == '__main__':
    # Collect numbers from user
    num = int(input("Enter Number:"))
    if num < 0:
        print("Enter a positive number.")
    else:
        result = sum_numbers_recursive(num)
        print(f"The sum of numbers from {num} is: {result}")
