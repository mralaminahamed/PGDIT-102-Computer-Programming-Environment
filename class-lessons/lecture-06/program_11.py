# Write a Python program to calculate the value of 'a' to the power of 'b‘using
# recursion.

def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        # 10 ^ 4
        # 10 * 10 * 10 * 10
        return a * power(a, b - 1)


# Collect numbers from user
base = int(input("Enter Base Number:"))
exponent = int(input("Enter Exponent Number:"))

# Calculate the power of numbers : example = 10^1
result = power(base, exponent)
# print(f"{base} raised to the power of {exponent} is: {result}")
print(base, 'raised to the power of', exponent, 'is:', result)

