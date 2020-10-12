cont = int(input())
a = 1
b = 1
c = 1
for cont in range(0,cont):
		print(a,b,c)
		b = b + 1
		c = c + 1
		print(a,b,c)
		a = a + 1
		b = b + (a-1) * 2
		c = a * b