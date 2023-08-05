# Write a Python program to check whether a given key already exists in a
# dictionary.

employee = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# Get input from the user.
user_input = input("Enter a key: ")

if '' != user_input:
    if user_input in employee.keys():
        print(f"The key '{user_input}' is exists in the Dictionary")
    else:
        print(f"The key '{user_input}' is not exists in the Dictionary")
else:
    print(f"The key is not be empty")
