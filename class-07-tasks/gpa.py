def calculate_result(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks, final):
    in_course_mark = in_course_calculate(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks)
    final_marks = final_calculate(in_course_mark, final)
    return gpa_calculate(final_marks)


def in_course_calculate(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks):
    # Average of quiz marks (sum of quiz marks * 2) multiplied by 3
    total_quiz_marks = ((q1_marks + q2_marks + q3_marks) * 2) / 3
    return attendance_marks + total_quiz_marks + lab_marks


def final_calculate(in_course_mark, final):
    return in_course_mark + final


def gpa_calculate(final_marks):
    # Calculate GPA based on the final marks
    if final_marks >= 90:
        gpa = 4.0
    elif final_marks >= 80:
        gpa = 3.7
    elif final_marks >= 70:
        gpa = 3.3
    elif final_marks >= 60:
        gpa = 3.0
    elif final_marks >= 50:
        gpa = 2.7
    elif final_marks >= 40:
        gpa = 2.3
    else:
        gpa = 0.0
    return gpa


if __name__ == '__main__':
    # Collect input from the professor
    attendance_mark = int(input("Enter the attendance mark (out of 10): "))
    quiz_marks = input("Enter the quiz mark (out of 15) with comma: ")
    lab_mark = int(input("Enter the lab mark (out of 10): "))
    final_mark = int(input("Enter the final mark (out of 50): "))

    # Split the quiz mark using the comma separator
    values_list = quiz_marks.split(',')

    # Convert elements to integers using list comprehension
    int_values_list = [int(value) for value in values_list]

    # Calculate GPA
    gpa_result = calculate_result(attendance_mark, *int_values_list, lab_mark, final_mark)

    # Show result
    print(f"GPA for this student is {gpa_result:.2f}")
