def sum_numbers_recursive(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers_recursive(n - 1)


if __name__ == '__main__':
    num = 5
    result = sum_numbers_recursive(num)
    print(f"The sum of numbers from 1 to {num} is: {result}")