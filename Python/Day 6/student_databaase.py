student={}
for i in range(3):
    name=input("enter the name of student")
    marks=float(input("enteer the marks of student"))

    student[name]=marks
print("student database")

for name,marks in student.items():
    print(f" {student}: {marks}")