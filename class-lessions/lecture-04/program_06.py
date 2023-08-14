# Write a program to read 10 numbers from the keyboard and find their
# sum and average.

sum = 0
i = 1
while i <= 10:
    number = int(input('Enter number: '))
    sum = sum + number
    i = i + 1

print('Sum = ', sum)
avg = sum / 10
print('Average = ', avg)
