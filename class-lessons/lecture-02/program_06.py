# Question: Write a program that takes hours and minutes as input, and calculates the total number of minutes.

# Show message to the screen for getting hours and minutes.
hours = int(input('Enter the hours of time: '))
minutes = int(input('Enter the minutes of time: '))

# Calculate the perimeter of a rectangle and assign variable.
# formula: H = 60minutes
hourToMinutes = 60 * hours
totalMinutes = hourToMinutes + minutes

# Show the output.
print("The total minutes of time is : ", totalMinutes)
