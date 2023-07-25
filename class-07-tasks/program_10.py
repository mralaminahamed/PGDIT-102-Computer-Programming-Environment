def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


if __name__ == '__main__':
    num1 = 48
    num2 = 18
    result = gcd_recursive(num1, num2)
    print(f"The GCD of {num1} and {num2} is: {result}")