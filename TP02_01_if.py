a, b, c, d = map(int,input().split())
resto = a%2
if b > c and d > a and (c+d) > (a+b) and c > 0 and d > 0 and resto == 0:
		print("Valores aceitos")
else : 
	print("Valores nao aceitos")