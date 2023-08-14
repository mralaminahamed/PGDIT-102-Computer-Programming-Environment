# A student will not be allowed to sit in exam if his/her attendence is less
# than 70%. Take following input from user & print percentage of class
# attended. Is student is allowed to sit in exam or not?
# • Number of classes held
# • Number of classes attended.

# Collect the held classes and attended classes from the student.
totalClasses = int(input("Enter the classes held:"))
attendance = int(input("Enter the total attendance:"))

# assign the variable for percentage.
percentage = attendance / totalClasses * 100


# Calculate the bonus for employee with service year
if percentage < 70:
    # Show the message to the screen.
    print('You are not allowed in the exam.')
else:
    # Show the message to the screen.
    print('You are allowed in the exam.')