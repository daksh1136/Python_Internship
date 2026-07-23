try:
    n1=int(input("enter the first number:"))
    n2=int(input("enter the second number:"))
    print("calculater menu")
    print(" 1. add \n 2. subtract \n 3. multiply \n 4.divide ")
    choice=int(input("enter your choice:"))
    if choice==1:
        print( n1+n2)
    elif choice==2:
     print( n1-n2)
    elif choice==3:
     print( n1*n2)
    elif choice==4:
       print( n1/n2)
    else:
       print("enter the valid number")
except :
   print("check the number once")
finally:
   print("program executed")
   
 
     

             