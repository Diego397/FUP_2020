while True:
		lista = input().split()
		if len(lista) == 1:
				break
		else:
				a = int(lista[0])
				b = int(lista[1])
				c = int(lista[2])
		acasa = a * b
		ater = acasa * 100/c
		lter = ater ** (1/2)
		print(int(lter))