vimpar = [0] * 5
vpar = [0] * 5
contador1 = 0
contadorp = 0
contadori = 0
while contador1 < 15:
		n = int(input())
		resto = n % 2
		if resto == 0:
				vpar[contadorp] = n
				contador1 = contador1 + 1
				contadorp = contadorp + 1
				if contadorp == 5:
						for contadorp2 in range(0,5):
								print("par[{:.0f}] = {:.0f}".format(contadorp2,vpar[contadorp2]))
						vpar = [0] * 5
						contadorp = 0
		else:
				vimpar[contadori] = n
				contador1 = contador1 + 1
				contadori = contadori + 1
				if contadori == 5:
						for contadori2 in range(0,5):
								print("impar[{:.0f}] = {:.0f}".format(contadori2,vimpar[contadori2]))
						vimpar = [0] * 5
						contadori = 0
for contadori3 in range(0,5):
								if vimpar[contadori3] != 0:
										print("impar[{:.0f}] = {:.0f}".format(contadori3,vimpar[contadori3]))
for contadorp3 in range(0,5):
								if vpar[contadorp3] != 0:
										print("par[{:.0f}] = {:.0f}".format(contadorp3,vpar[contadorp3]))