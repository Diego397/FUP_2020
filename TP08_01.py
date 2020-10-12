w, x, y, z = map(int,input().split())
lista = [w, x, y, z]
lista.sort()
a = lista[-1] 
b = lista[-2]
c = lista[-3]
d = lista[-4]
if a < (b+c) or a < (b+d) or a < (c+d) or b < (c+d):
		print("S")
else:
		print("N") 