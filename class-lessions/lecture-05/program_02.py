# Write a program to find the avg marks of students in a class using list.

numbers_list = [10, 20, 30, 40, 50]
total_sum = 0

for num in numbers_list:
    total_sum += num

print(f"The avg marks of students in a class is: {total_sum // 5}")
