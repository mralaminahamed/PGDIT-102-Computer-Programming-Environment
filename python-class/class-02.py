# data_1 = 34
# data_2 = 87
#
# inputData1 = int(input("enter number one: "))
# inputData2 = int(input("enter number two: "))
#
# print(inputData1 + inputData2)
# print(inputData1 - inputData2)
# print(inputData1 * inputData2)
# print(inputData1 / inputData2)
# print(inputData1 % inputData2)

# Write a program to return the quotient and remainder of a division.
# quotient = ভাগফল
# remainder = ভাগশেষ

# Write a program that converts Centigrade to Fahrenheit.
# (0°C × 9/5) + 32 = 32°F
# (32°F − 32) × 5/9 = 0°C
# centigrade = int(input("Enter the centigrade: "))
# fer = (centigrade * 9/5) + 32
# print(fer)


# Write a program that prints the perimeter of a rectangle with its height
# and width as input.

# Write a program that takes hours and minutes as input, and calculates the
# total number of minutes.
#
# hours= int(input("enter the hours: "))
# minutes= int(input("enter the minutes: "))
#
# total_hours = hours * 60
#
# print(total_hours + minutes)

# Write a program in that takes minutes as input, and display the total
# number of hours and minutes.
# minutes= int(input("enter the minutes: "))
# print(minutes // 60)
# print(minutes % 60)

# Write a program in that reads a forename, surname and year of birth and
# display the names and the year one after another sequentially.

# forename = input("Enter your forename: ")
# surname = input("Enter your surname: ")
# year_of_birth = input("Enter your year of birth: ")
#
# print("Your name is ", forename, surname, 'and your date of birth is', year_of_birth)
# print(f"Your name is {forename} {surname} and your date of birth is {year_of_birth}")

#
# number = 40
#
# if number > 80:
#     print("A+")
#
# if number > 70:
#     print("A")
#
# if number > 60:
#     print("A-")
#
# if number > 50:
#     print("B")
#
# if number > 40:
#     print("D")
#
# if number > 33:
#     print("E")
#
# if number > 80:
#     print("A+")
# elif number > 70:
#     print("A")
# elif number > 60:
#     print("A-")
# elif number > 50:
#     print("B")
# elif number > 40:
#     print("D")
# elif number > 33:
#     print("E")
# else:
#     print("F")

#
# # Write a program to find the largest of three numbers.
# number1 = float(input("Enter your number 01: "))
# number2 = float(input("Enter your number 02: "))
# number3 = float(input("Enter your number 03: "))
#
# largest_number = ''
#
# if number1 > number2:
#     largest_number = number1
# else:
#     largest_number = number2
#
# if number3 > largest_number:
#     largest_number = number3
#
#
# print(largest_number)
#
# # Write a program to find the smallest of three numbers.
# number1 = float(input("Enter your number 01: "))
# number2 = float(input("Enter your number 02: "))
# number3 = float(input("Enter your number 03: "))
#
# largest_number = ''
#
# if number1 < number2:
#     largest_number = number1
# else:
#     largest_number = number2
#
# if number3 < largest_number:
#     largest_number = number3
#
#
# print(largest_number)


# A company decided to give bonus to employees based on the following
# conditions:
# i. 10% of salary if year of service is more than 5 years
# ii. 5% of salary if year of service is more than 3 years.
# • Ask user for their salary and year of service and print the total amount.

# employee_salary = int(input("Enter employee salary: "))
# employee_year = int(input("Enter employee service year: "))
#
#
# if employee_year >= 5:
#     print("bonus: ", employee_salary * .10)
#     print("salary: ", employee_salary + (employee_salary * .10))
# elif employee_year >= 3:
#     print("bonus: ", employee_salary * .05)
#     print("salary: ", employee_salary + (employee_salary * .05))
# else:
#     print("bonus: 0")
#     print("salary: ", employee_salary)
#


# A student will not be allowed to sit in exam if his/her attendence is less
# than 70%. Take following input from user & print percentage of class
# attended. Is student is allowed to sit in exam or not?
# • Number of classes held
# • Number of classes attended.
#
# number_of_classes = int(input("Enter the number of classes held: "))
# number_of_classes_attended = int(input("Enter the number of classes attended: "))
#
# percentage = (number_of_classes_attended / number_of_classes) * 100
#
# print(percentage)
#
# if percentage > 70:
#     print("A student will be allowed to sit in exam ")
#     if percentage > 70:
#         print("A student will be allowed to sit in exam ")
#     else:
#         print("A student will not be allowed to sit in exam ")
# else:
#     print("A student will not be allowed to sit in exam ")
#


lists = [10, 10, 10, 10, 10, 20]
for item in lists:
    print(item)


data = 0

while data > 5:
    print(data)
    data = data + 1






i = 1
while i < 6:
  print(i)
  i += 1