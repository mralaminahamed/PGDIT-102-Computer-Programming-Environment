def calculate_result(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks, final):
    in_course_mark = in_course_calculate(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks)
    final_marks = final_calculate(in_course_mark, final)
    gpa = gpa_calculate(final_marks)
    return gpa


def in_course_calculate(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks):
    total_quiz_marks = ((q1_marks + q2_marks + q3_marks) * 2) / 3
    in_course_total = attendance_marks + total_quiz_marks + lab_marks
    return in_course_total


def final_calculate(in_course_mark, final):
    final_marks = in_course_mark + final
    return final_marks


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
    attendance_mark = 10
    quiz_marks = [15, 20, 25]  # Average of quiz marks (sum of quiz marks * 2) multiplied by 3
    lab_mark = 10
    final_mark = 50

    # Calculate GPA
    gpa_result = calculate_result(attendance_mark, *quiz_marks, lab_mark, final_mark)

    # Show result
    print(f"GPA for this student is {gpa_result:.2f}")
