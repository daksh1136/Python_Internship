class employee:
    def __init__(self,e_name,e_id,e_salary):
        self.name=e_name
        self.id=e_id
        self.salary=e_salary
    def info(self):
        print(f"employee name : {self.name}")
        print(f"employeee id: {self.id}")
        print(f"employeee salary :{self.salary}")



name=input("enter the name of employeee :")
id=int(input("enter the id of employee :"))
salary=int(input("enter the salary of employeee"))

one=employee(name,id,salary)
one.info()