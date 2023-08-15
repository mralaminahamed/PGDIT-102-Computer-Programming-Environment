# Create a list of marks of ten students.
# • Find the largest and smallest mark in the list.
# • Find the average mark of the students.
# • Sort the marks in ascending order.
# • Sort the marks in descending order.
# • Remove the smallest mark from the list.
# • Insert the average mark at the mid-position of the list.
# • Create another list of five students’ mark and merge the two lists.

# Assign a variable with a list of marks of ten students.
mark_list = [49, 48, 41, 44, 38, 27, 20, 28, 35, 45]

# Finding the largest number in the list
largest_mark = mark_list[0]
for mark in mark_list:
    if mark >= largest_mark:
        largest_mark = mark

print("Example 01: The largest mark is:", largest_mark)
print("Example 02: The largest mark is:", max(mark_list))

# Finding the smallest number in the list
smallest_mark = mark_list[0]
for mark in mark_list:
    if mark <= smallest_mark:
        smallest_mark = mark

print("Example 01: The smallest mark is:", smallest_mark)
print("Example 02: The smallest mark is:", min(mark_list))

# Finding the average number in the list
average_mark = 0
for mark in mark_list:
    average_mark += mark

print("Example 01: The average mark is:", (average_mark // 10))
print("Example 02: The average mark is:", (sum(mark_list) // 10))

# Sort the marks in ascending order.
sorted_list = mark_list.sort()
print("The marks in ascending order is:", mark_list)

# Sort the marks in descending order.
mark_list.sort(reverse=True)
print("Example 01: The marks in descending order is:", mark_list)
# print("Example 02: The marks in descending order is:", mark_list.reverse())

# Remove the smallest mark from the list.
mark_list.remove(min(mark_list))
print("Removed the smallest mark from the list is:", mark_list)

# Insert the average mark at the mid-position of the list.
print("Current average mark is:", (sum(mark_list) // 10))
mark_list.insert(len(mark_list) // 2, (sum(mark_list) // 10))
print("Inserted the average mark at the mid-position of the list is:", mark_list)


# Create another list of five students’ mark and merge the two lists.
new_mark_list = [42, 40, 32, 39, 43]
mark_list.extend(new_mark_list)
print("merged the two list is:", mark_list)
