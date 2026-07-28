class parent:
    def __init__(self,namee):
        self.name=namee


class child(parent):
     def __init__(self,name,course):
          super().__init__(name)
          self.course=course
          print(self.name)
          print(self.course)


b=child("daksh","enggg")
