class Student:

    school = "Galgotias University"

    def __init__(self, name):
        self.name = name


s1 = Student("Daksh")
s2 = Student("Rahul")

print(s1.school)
print(s2.school)