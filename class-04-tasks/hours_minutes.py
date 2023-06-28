# Collect the minutes from user.
minutes = int(input("Input the minutes:"))

# Calculate the minutes into hours and minutes
totalHours = minutes // 60
extraMinutes = minutes % 60

# Show the total hours and minutes in the screen;
print('The total hours from minutes is: ', totalHours)
print('The extra minutes from minutes is: ', extraMinutes)
