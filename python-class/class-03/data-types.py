# Float
float_number = 10.203
print(float_number)

float_number_2 = float("10.529")
print(float_number_2)
print(type(float_number_2))

# round (the_float_number, range)
money = round(float_number_2, 2)
print(money)

absolute_number = abs(-35.985)
print(absolute_number)

maximumNumber = max([10.85, 98.32, 5874.30 ])
print(maximumNumber)

minimumNumber = min([10.85, 98.32, 5874.30 ])
print(minimumNumber)

# Python3 program introducing f-string
val = 'Geeks'

print(f"{val}for{val} is a portal for {val}.")
print(val, 'for', val, 'is a portal for',val, '.' )

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")


