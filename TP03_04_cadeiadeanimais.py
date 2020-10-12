coluna = str(input())
tipo = str(input())
comida = str(input())
if coluna == "vertebrado":
		if tipo == "ave" and comida == "onivoro":
			print("pomba")
		elif tipo == "ave" and comida == "carnivoro":
			print("aguia")
		elif tipo == "mamifero" and comida == "herbivoro":
			print("vaca")
		elif tipo == "mamifero" and comida == "onivoro":
			print("homem")
elif coluna == "invertebrado":
		if tipo == "inseto" and comida == "hematofago":
			print("pulga")
		elif tipo == "inseto" and comida == "herbivoro":
			print("lagarta")
		elif tipo == "anelideo" and comida == "hematofago":
			print("sanguessuga")
		elif tipo == "anelideo" and comida == "onivoro":
			print("minhoca")