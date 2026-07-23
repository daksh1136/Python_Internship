try:
    file= open("sumbit.txt","r")
    file.read()
except FileNotFoundError as f:
    print(" file hai hi nhi read kaise krun")
finally:
    print(" program run completly")