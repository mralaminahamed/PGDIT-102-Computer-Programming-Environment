# Write a Python script to add a key to a dictionary.

# Initiate default variable with empty dictionary.
dicts = dict()

# Get input from the user.
user_input = input("Enter a key: ")

if '' != user_input:
    dicts.update([(1, user_input)])

print(dicts)


# Another example
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}
#
# # updates the value of key 2
# d.update(d1)
#
# print(d)
