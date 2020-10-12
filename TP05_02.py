a = 0
g = 0
d = 0
i = 0
while i != 4:
		i = int(input())
		if i >= 1 and i <= 3:
				if i == 1:
						a = a + 1
				elif i == 2:
						g = g + 1
				elif i == 3:
						d = d + 1
print("MUITO OBRIGADO")
print("Alcool: {:.0f}".format(a))
print("Gasolina: {:.0f}".format(g))
print("Diesel: {:.0f}".format(d))