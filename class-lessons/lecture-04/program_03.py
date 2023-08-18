# Write a program to find all odd numbers from 1 to N.

# Collect the number of times from user.
times = int(input("Enter the number of times: "))

# even = জোড়
# odd = বিজোড়
count = 1
while count <= times:
    # result = count % 2 == 1
    if count % 2:  # the output will be 1 for every odd number
        print(count)
    count += 1
