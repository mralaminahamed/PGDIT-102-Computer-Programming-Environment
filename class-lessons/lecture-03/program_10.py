# A company decided to give bonus to employees based on the following
# conditions:
# i. 10% of salary if year of service is more than 5 years
# ii. 5% of salary if year of service is more than 3 years.
# • Ask user for their salary and year of service and print the total amount.

# Collect the salary and service year from user.
basicSalary = int(input("Enter the basic salary:"))
serviceYear = int(input("Enter the service year:"))

# Calculate the bonus for employee with service year
if serviceYear >= 5:
    bonusSalary = basicSalary * (10 / 100)
elif serviceYear >= 3:
    bonusSalary = basicSalary * (5 / 100)
else:
    bonusSalary = 0

# Show the discount availability message to the screen.
print('Hurry!! You get the bonus is: ', bonusSalary)
print('Hurry!! You get the salary with bonus is: ', (basicSalary + bonusSalary))
