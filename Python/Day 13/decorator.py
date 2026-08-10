def gret(func):
    func()

    print("good morning")
    func()
    
    return func


@gret
def first():
    print("raaam raaam ji")
@gret
def second():
    print(" second decorator")


first()


print(first     )