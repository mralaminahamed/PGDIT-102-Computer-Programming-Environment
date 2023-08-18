# write a program using python to create a simple calculator

# Collect all numbers and operator for operation from user.
number1 = float(input('Input the first number:'))
number2 = float(input('Input the second number:'))
operator = input('Input the operator from (+, -, *, /, %):')

result = ''
if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '*':
    result = number1 * number2
elif operator == '/':
    result = number1 / number2
elif operator == '%':
    result = number1 % number2
else:
    print('Invalid choice ')

if result != '':
    print('The result is: ', result)
else:
    print('Unable to calculate the result ')
