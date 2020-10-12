a, b, c = map(float,input().split())
delta = float((b**2 - 4 * a * c))
raiz = delta**(1/2)
if delta >= 0 and a != 0 :
		r1 = ((-b + raiz)/(a*2))
		r2 = ((-b - raiz)/(a*2))
		print("R1 = {:.5f}".format(r1))
		print("R2 = {:.5f}".format(r2))
else :
		print("Impossivel calcular")