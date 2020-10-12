lista = [0] * 1000
n = int(input())
a = 0
i = 0
marc = 2
while marc == 2:
		while i < 1000 and a < n:
				lista[i] = a
				a = a + 1
				i = i + 1
		a = 0
		if i == 1000:
				marc = 1
for cont in range(0,1000):
		print("N[{:.0f}] = {:.0f}".format(cont,lista[cont]))