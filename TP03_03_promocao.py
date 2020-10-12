valori = float(input())
if 0 < valori <= 400.00:
	valorn = 1.15*valori
	perc = 15
elif 400.00 < valori <= 800.00:
	valorn = 1.12*valori
	perc = 12
elif 800.00 < valori <= 1200.00:
	valorn = 1.1*valori
	perc = 10
elif 1200.00 < valori <= 2000.00:
	valorn = 1.07*valori
	perc = 7
else:
	valorn = 1.04*valori
	perc = 4
diferenca = valorn - valori
print("Novo salario: {:.2f}".format(valorn))
print("Reajuste ganho: {:.2f}".format(diferenca))
print("Em percentual: {:.0f} %".format(perc))