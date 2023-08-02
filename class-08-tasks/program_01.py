# Write a Python program to calculate the length of a string.

def calculate_string_length(input_string):
    return len(input_string)


# Get input from the user
user_input = input("Enter a string: ")

# Calculate and display the length of the string
string_length = calculate_string_length(user_input)
print(f"The length of the string is: {string_length}")
