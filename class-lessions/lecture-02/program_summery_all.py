# Collect the two numbers from user.
numberOne = int(input("Enter the number one: "))
numberTwo = int(input("Enter the number two: "))

# calculate total sum.
result = numberOne + numberTwo

# Collect the desired number from user for compare with result.
userInput = int(input("Enter the your desired number: "))

if result == userInput:
    print("Congratulation!! Your desired is matched with result.")
else:
    print("Ohh! Sorry not matched with your number.")
    print("The number will be : ", result)


