# Collect the terms from user.
term = int(input('Enter the number:'))

# Assign required variables.
first = 0
second = 1
count = 2

print(first, second, count)

while count < term:
    newNumber = first + second

    # show new number.
    print(newNumber)

    # Update the count numbers.
    count = count + 1

    # Update first and second numbers.
    first = second
    second = newNumber
