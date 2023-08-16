# Write a program to display the first N natural numbers.

# Natural numbers
# A part of the number system which includes all the positive integers from 1 till infinity and
# are also used for counting purpose. It does not include zero (0). In fact, 1,2,3,4,5,6,7,8,9…., are also called
# counting numbers.

# Collect the number of times from user.
times = int(input("Enter the number of times: "))

count = 1
while count <= times:
    print(count)
    count += 1
