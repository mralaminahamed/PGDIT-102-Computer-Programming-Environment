def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a * power(a, b - 1)


if __name__ == '__main__':
    # Collect numbers from user
    base = int(input("Enter Base Number:"))
    exponent = int(input("Enter Exponent Number:"))

    # Calculate the power of numbers
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
