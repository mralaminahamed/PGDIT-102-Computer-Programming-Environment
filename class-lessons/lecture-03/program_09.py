# A school has the following rules for grading system:
# i) Below 50 – F; ii) 50 to 60 – D; iii) 60 to 70 – C; iv) 70 to 80 – B; v) Above 80 – A
# • Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter your marks: "))

if marks > 80:
    print("You got A Grade.")
elif 80 > marks > 70:
    print("You got B Grade.")
elif 70 > marks > 60:
    print("You got C Grade.")
elif 60 > marks > 50:
    print("You got D Grade.")
# elif marks > 50:
#     print("F")
else:
    print("You got F Grade.")
