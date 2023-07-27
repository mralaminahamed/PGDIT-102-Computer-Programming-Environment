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


def contains_comma(input_string):
    return ',' in input_string


if __name__ == '__main__':
    try:
        # Collect input from the professor
        attendance_mark = int(input("Enter the attendance mark (out of 10): "))
        quiz_marks = input("Enter the quiz mark (out of 15) with comma: ")
        lab_mark = int(input("Enter the lab mark (out of 10): "))
        final_mark = int(input("Enter the final mark (out of 50): "))

        print("-----------------------------------------------")

        if attendance_mark > 10:
            print(f"Invalid attendance mark({attendance_mark}). Marks will be not greater than 10.")

        if lab_mark > 10:
            print(f"Invalid lab mark({lab_mark}). Marks will be not greater than 10.")

        if final_mark > 50:
            print(f"Invalid lab mark({final_mark}). Marks will be not greater than 50.")

        if contains_comma(quiz_marks):
            # Split the quiz mark using the comma separator
            values_list = quiz_marks.split(',')

            # Convert elements to integers using list comprehension
            int_values_list = [int(value) for value in values_list]
            quiz_marks_valid = 1

            for quz_mark in int_values_list:
                if quz_mark > 15:
                    quiz_marks_valid = 0
                    print(f"Invalid quiz mark({quz_mark}). Marks will be not greater than 15.")

            if quiz_marks_valid == 1:
                # Total Marks
                in_course_mark = in_course_calculate(attendance_mark, *int_values_list, lab_mark)
                final_marks = final_calculate(in_course_mark, final_mark)

                # Calculate GPA
                gpa_result = gpa_calculate(final_marks)

                # Show result
                print(f"Total mark for this student is {int(final_marks)}")
                print(f"GPA for this student is {gpa_result:.2f}")

        else:
            print("Invalid quiz mark. QUiz mark will be contains command (,).")

    except:
        print("An exception occurred")
