n = int(input())
for n in range(0,n):
		i = int(input())
		resto = i % 2
		if resto == 0:
				paridade = "EVEN"
		else:
				paridade = "ODD"
		if i > 0:
				valor = "POSITIVE"
		elif i == 0:
				valor = "NULL"
		else:
				valor = "NEGATIVE"
		if i == 0:
				print(valor)
		else:
				print(paridade, valor)