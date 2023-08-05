# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

# Initiate default variable with empty dictionary.
dicts = dict()

# Get input from the user.
user_input = input("Enter a key: ")

if '' != user_input:
    if user_input.isdigit():
        dicts.update([(int(user_input), (int(user_input) * int(user_input)))])
        print(dicts)
    else:
        print(f"The key {user_input} is not be a number")
else:
    print("The key is not be empty")
