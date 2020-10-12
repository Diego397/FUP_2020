l = int(input())
t = str(input())
soma = 0
media = 0
m = [[0]*12 for i in range(12)]
for cont1 in range(12):
		for cont2 in range(12):
				m[cont1][cont2] = float(input())
for cont3 in range(12):
		soma = soma + m[l][cont3]
if t == "S":
		print(soma)
media = soma/12
if t == "M":
		print("{:.1f}".format(media))