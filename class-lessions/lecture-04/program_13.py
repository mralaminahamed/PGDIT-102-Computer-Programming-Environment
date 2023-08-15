# Write a program to determine whether a given number is prime or not.

# Prime numbers
# natural numbers that are divisible by only 1 and the number itself. In other words, prime numbers are
# positive integers greater than 1 with exactly two factors, 1 and the number itself. Some of the prime numbers
# include 2, 3, 5, 7, 11, 13, etc. Always remember that 1 is neither prime nor composite.

# Collect a number from user.
number = int(input("Enter the number: "))

if number <= 1:
    print("This number is not a prime")
elif number > 1:
    # check the factors.
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime")
            break
    else:
        print(number, "is a prime")
