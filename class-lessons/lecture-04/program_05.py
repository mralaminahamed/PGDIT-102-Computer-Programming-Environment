# Write a program to find the sum of first N natural numbers.

# Collect the number from user.
number = int(input("Enter the number: "))
if number <= 0:
    print("Number must be a positive integer")
else:
    count = 1
    result = 0
    while count <= number:
        result += count
        count += 1

    print("The result is: ", result)


# Another examples.
print((number * (number + 1)) // 2)