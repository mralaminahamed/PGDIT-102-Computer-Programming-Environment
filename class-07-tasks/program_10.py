def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


if __name__ == '__main__':
    # Collect numbers from user
    number1 = int(input("Enter First Number:"))
    number2 = int(input("Enter Second Number:"))

    # Calculate the GCD of numbers
    result = gcd_recursive(number1, number2)
    print(f"The GCD of {number1} and {number2} is: {result}")
