class animal():
    def sound(self):
        print("aninmal is making sound")

class dog(animal):
    def sound(self):
        print("dog is barking")

class cat(animal):
    def sound(self):
        print("cat is meowing")

animal=[dog(),cat()]
for animal in animal:
    animal.sound() 