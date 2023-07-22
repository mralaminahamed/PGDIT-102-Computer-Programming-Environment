
def calculate_result( attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks, final ):
    in_course_mark = in_course_calcate(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks)
    final_marks = final_calculate( in_course_mark, final )
    gpa = gpa_calculate(final_marks)

def in_course_calcate(attendance_marks, q1_marks, q2_marks, q3_marks, lab_marks):
    # calculate in course total

def final_calculate( in_course_mark, final ):
    # calculate in final

def gpa_calculate( final_marks ):
    # calculate in final marks



if __name__ == '__main__':
    # show prompt and collect input from professor
    # a student will be get
    # attendense mark = 10
    # quiz mark = 15, but each mark multiplication with 2 to get avarege
    # lab mark = 10
    # final mark = 50

    # show reslt like this format
    # enter the flowing marks, at q1 q
    # gpa for this student '' is ''
