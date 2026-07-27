class car:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def info(self):
        print(f"carr name:{self.name}")
        print(f" car model: {self.model}")
        print(f" car pricev : {self.price}")


toyota=car("fortuner",2026,5500000)
toyota.info()