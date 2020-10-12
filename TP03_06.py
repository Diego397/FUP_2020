salario = float(input())
if 0 < salario <= 2000.00:
		print("Isento")
elif 2000.00 < salario <= 3000.00:
		taxa = (salario - 2000.00) * (8/100)
		print("R$ {:.2f}".format(taxa))
elif 3000.00 < salario <= 4500.00:
		taxa = 1000.00 * (8/100) + (salario - 3000.00) * (18/100)
		print("R$ {:.2f}".format(taxa))
elif 4500.00 < salario :
		taxa = 1000.00 * (8/100) + (1500.00) * (18/100) + (salario - 4500.00) * (28/100)
		print("R$ {:.2f}".format(taxa))