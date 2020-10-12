o = str(input())
soma = 0
media = 0
m = [[0]*12 for i in range(12)]
for cont1 in range(12):
		for cont2 in range(12):
				m[cont1][cont2] = float(input())
				if cont1 >= cont2 and cont1 + cont2 > 11:
					soma = soma + m[cont1][cont2]
				elif cont2 > cont1 and cont1 + cont2 > 11:
					soma = soma + m[cont1][cont2]

media = soma/66
if o == "S":
		print("{:.1f}".format(soma))
elif o == "M":
		print("{:.1f}".format(media))