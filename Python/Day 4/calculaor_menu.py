def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

a=float(input("enter thee value of a :"))
b=float(input("enter the value of b"))
print("1 . for add")
print(" 2. for subtract")
print("3.  for multiplication")
print("4.  for divide")
choice=int(input("enter what do u want to do"))
if choice==1:

   print(" add  ",add(a,b))
elif choice==2:\
    print("subtract",sub(a,b))
elif choice ==3:
       print("mult",mult(a,b))
elif choice==4:
 print("divide",div(a,b)) 
else:
    print("invalid input")