def pass_word__cherccker(func):

    def inner():
        password = input("Enter your password: ")
        if password == "1234":
            print("Access granted")
            func()
        else:
            print("Access denied")
    return inner

@pass_word__cherccker
def dasshhbourd():
    print("Welcome to the dashboard!")

dasshhbourd()