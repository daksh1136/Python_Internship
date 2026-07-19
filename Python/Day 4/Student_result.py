def student_grade_system(marks):
 if marks>90 and marks<100:
    return "A"
 elif marks>80 and marks<90:
    return "B"
 elif marks>70 and marks<80:
    return "C"
 elif marks>60 and marks<70:
     return "D"
 elif marks>50 and marks<60:
    return "E"
 else:
    return fail
 



grade=0
marks=float(input("enter the marks of student"))
grade=student_grade_system(marks)
print(grade)
print(marks)
