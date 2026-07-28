class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary


    def info(self):
        print( self.name)
        print(self.salary)


e1=employee("daksh",25000)
e2=employee("krish",50000)
e1.info()
e2.info()