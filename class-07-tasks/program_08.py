def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    # Collect numbers from user
    num = int(input("Enter Number:"))
    result = factorial_recursive(num)
    print(f"The factorial of {num} is: {result}")