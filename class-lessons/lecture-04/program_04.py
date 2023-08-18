# Write a program to find all even numbers from 1 to N.

# Collect the number of times from user.
times = int(input("Enter the number of times: "))

count = 1
while count <= times:
    if count % 2 == 0:  # the output will be 1 for every odd number
        print(count)
    count += 1
