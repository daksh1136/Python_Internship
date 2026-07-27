class student:
    def __init__(self):
       
        print("constructor called")

    def info(self):
        self.name="daksh"
        self.number="24scse118"
        print(self.name)
        print(self.number)


aa=student()
aa.info()