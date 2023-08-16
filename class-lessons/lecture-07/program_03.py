# Write a Python program to remove the nth index character from a
# nonempty string.

def remove_nth_character(input_string, n):
    if n < 0 or n >= len(input_string):
        return "Invalid index"

    return input_string[:n] + input_string[n + 1:]


# Get input from the user
user_input = input("Enter a string: ")
index_string = input("Enter the index of the character to remove: ")


if user_input == '':
    print(f"The string can not be empty.")
elif not index_string.isdigit():
    print("Invalid index. Index must be a number")
else:
    # Remove the character at the specified index and display the modified string
    modified_string = remove_nth_character(user_input, int(index_string))
    print(f"The modified string is: {modified_string}")
