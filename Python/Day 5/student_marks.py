list=[]
for i in range(5):
    mark=float(input(f"enter the marks of {i+1}  student :"))
    list.append(mark)

print("""---------result--------""")
print(f" maximum marks:{max(list)}")
print(f" manimum marks:{min(list)}")
print(list)
print("the sum of marks is :",sum(list))
print("avg marks ",sum(list)/len(list))



