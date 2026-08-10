studs=["Alice", "Bob", "Charlie", "David", "Eve","11"]
it=iter(studs)
print(it.__next__())

print(it.__next__())
print(it.__next__())
print(it.__next__())

print(next(it))
print(it.__next__())

print(type(it))