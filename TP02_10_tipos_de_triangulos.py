x, y, z = map(float,input().split())
lista = [x,y,z]
lista.sort()
a = lista[-1]
b = lista[-2]
c = lista[-3]
if a >= (b + c):
		print("NAO FORMA TRIANGULO")
else :		
		if (a**2) == (b**2) + (c**2) :
				print("TRIANGULO RETANGULO")  
		if (a**2) > (b**2) + (c**2) :
				print("TRIANGULO OBTUSANGULO")
		if (a**2) < (b**2) + (c**2) :
				print("TRIANGULO ACUTANGULO")
		if a == b == c :
				print("TRIANGULO EQUILATERO")
		if (a == b and a != c) or (a == c and a != b) or (c == b and c != a) :
				print("TRIANGULO ISOSCELES")