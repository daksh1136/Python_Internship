set1={1,2,3,4,5,6,7,8,9,0}
set2={2,4,6,8,10,12}
set3={1,3,5,7,11,9}
print("printing  of each sets")
print(set1)
print(set2)
print(set3)
print("lenght of each sets")

print(len(set1))
print(len(set2))
print(len(set3))

set1.remove(0)
print(set1)
print(set2.pop())
print("union")

print(set1.union(set2))
print(set2.union(set3))
print(set1.union(set2.union(set3)))
print("intersection")
print(set1.intersection(set2))
print(set2.intersection(set3))
print(set1.intersection(set2.intersection(set3)))

