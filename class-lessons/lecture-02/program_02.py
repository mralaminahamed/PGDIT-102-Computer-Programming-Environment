# Question: Write a program to return the quotient and remainder of a division.

# Show message to the screen for getting two input numbers.
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

# Calculate this two number quotient and remainder of a division,
# and assign separate variables.
# quotient = ভাগফল, remainder = ভাগশেষ
quotient = number1 // number2
remainder = number1 % number2

# Show the output in the separate lines.
print("The quotient is : ", quotient)
print("The remainder is : ", remainder)
