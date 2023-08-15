# Write a program to read 10 numbers from the keyboard and find their
# sum and average.

sums = 0
i = 1
while i <= 10:
    number = int(input('Enter number: '))
    sums += number
    i = i + 1

print('Sum = ', sums)
avg = sums / 10
print('Average = ', avg)
