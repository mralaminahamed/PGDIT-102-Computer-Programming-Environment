# Write a program to display the multiplication table of a given integer.

# Collect the target number for multiplication table.
N = int(input('Enter number: '))
i = 1

while i <= 10:
    # Display the multiplication.
    print(N, '*', i, '=', N * i)
    i = i + 1
