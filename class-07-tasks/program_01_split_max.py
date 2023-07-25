# Collect any three numbers from end user.
numbers = input("Enter numbers: ")

# Split the numbers using the comma separator
# and convert elements to integers using list comprehension
values_list = numbers.split(',')
int_values_list = [int(value) for value in values_list]

# Show the max number from the numbers.
print(max(*int_values_list))
