notes=input("welcome to yourr dairy write about youur day")
with open('sample.txt','a') as file:
 file.write(notes +"\n")


print("notes submitted scuccesfully")

