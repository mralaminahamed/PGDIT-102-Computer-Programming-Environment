def power_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recursive(a, b - 1)

if __name__ == '__main__':
    base = 2
    exponent = 3
    result = power_recursive(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")