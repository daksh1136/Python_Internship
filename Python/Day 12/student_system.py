class student:
    total_students=0
    def __init__(self,name):
        self.name=name
        student.total_students+=1


    @classmethod
    def count(self):
        print(f"total numberof ibject of same classs is {self.total_students}")


student("daksh")
student("tud")
student.count()
