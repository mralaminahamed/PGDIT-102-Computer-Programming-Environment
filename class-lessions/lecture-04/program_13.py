# Write a program to determine whether a given number is prime or not.

# Collect a number from user.
number = int(input("Enter the number: "))

if number <= 1:
    print("this number is not a prime")
elif number > 1:
    # check the factors.
    for i in range(2, number):
        if (number % i) == 0:
            print(i, " is not a prime")
            break
    else:
        print(number, " is a prime")
