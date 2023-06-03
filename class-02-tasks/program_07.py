# Show message to the screen for getting minutes.
minutes = int(input('Enter the minutes of time: '))

# Calculate total number of minutes. and assign variable.
# formula: H = 60minutes
minutesToHours = minutes // 60
extraMinutes = minutes % 60

# Show the output.
print("The total number of hours is : ", minutesToHours)
print("The total number of minutes is : ", extraMinutes)
