name=input("enter the name of student:")
marks=float(input("enter the marks of student:"))
with open("sample.txt","a") as file:
    file.write(f" {name} - {marks}")

print("record updated")