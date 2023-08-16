# Write a Python program to get a string made of the first 2 and last 2
# characters of a given string. If the string length is less than 2, return the
# empty string instead.

def get_first_and_last_chars(input_string):
    if len(input_string) < 2:
        return ""

    first_chars = input_string[:2]
    last_chars = input_string[-2:]

    return first_chars + last_chars


# Get input from the user
user_input = input("Enter a string: ")

# Get the modified string and display it
modified_string = get_first_and_last_chars(user_input)
print(f"The modified string is: {modified_string}")
