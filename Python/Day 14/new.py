count = 20
a, b = 0, 1

for _ in range(count):
	print(a)
	a, b = b, a + b
