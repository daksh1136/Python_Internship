print("__________Student grade system-------------")
name=input("enter the name of student :")
m1=float(input("enter the marks of 1st subject :"))
m2=float(input("enter the marks of 2nd subject :"))

m3=float(input("enter the marks of 3rd subject :"))
total=m1+m2+m3
percentage=total/3


if percentage>90:
    grade="A"
elif percentage>80:
    grade="B"
elif percentage>70:
    grade="C" 
elif percentage>60:
    grade="D"
elif percentage>50:
    grade="E"
else:
    grade="FAIL"
print(f"the name of student is :{name}")
print(f"the total marks of {name} is {total}")
print(f"the percentage of {name }is {percentage}")
print(f" the grade of {name} is {grade}")
print("-----------------------------END--------------------------")

