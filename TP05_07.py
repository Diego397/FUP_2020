x = float(input())
n = [0] * 100
n[0] = x
print("N[{:.0f}] = {:.4f}".format(0,n[0]))
for cont in range(1,100):
		n[cont] = (n[cont-1] / 2)
		print("N[{:.0f}] = {:.4f}".format(cont,n[cont]))