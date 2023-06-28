# Collect the salary and service year from user.
basicSalary = int(input("Enter the basic salary:"))
serviceYear = int(input("Enter the service year:"))

# Calculate the bonus for employee with service year
if serviceYear >= 5:
    bonusSalary = basicSalary * .1
elif serviceYear >= 3:
    bonusSalary = basicSalary * .05
else:
    bonusSalary = 0

# Show the discount availability message to the screen.
print('Hurry!! You get the bonus is: ', bonusSalary)
print('Hurry!! You get the salary with bonus is: ', (basicSalary + bonusSalary))
