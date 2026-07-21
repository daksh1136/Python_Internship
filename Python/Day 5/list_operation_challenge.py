list=[]
for  i in range(5):
    element=float(input(f"enter the {i+1} number:"))
    list.append(element)
print(list)
print("the sorted version of list is : ")
print(sorted(list))
print(f" the largest in list is {max(list)}")
print(f" the smallest in list is {min(list)}")
print(f"the sum of all nukber is {sum(list)}")
