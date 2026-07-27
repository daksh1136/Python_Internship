class student:
    def __init__(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
        print("constructor  called")
    def data(self):
        print(self.name)
        print(self.roll)
        print(self.age)


a_student=student("daksh",1180562,20)
a_student.data()
print(a_student.name)

        