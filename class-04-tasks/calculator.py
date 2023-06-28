number1 = float(input('Input the first number:'))
number2 = float(input('Input the second number:'))
operator = input('Input the operator from (+, -, *, /, %):')

result = ''
if operator == '+':
    result = number1 + number2

if operator == '-':
    result = number1 - number2

if operator == '*':
    result = number1 * number2

if operator == '/':
    result = number1 / number2

if operator == '%':
    result = number1 % number2

if result != '':
    print('The result is: ', result)
else:
    print('Unable to calculate the result ')
