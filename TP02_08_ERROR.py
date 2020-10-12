a, b, c = map(float,input().split())
p = a + b + c
A = ((a + b) * c)/2
if a + b <= c or a + c <= b or b + c <= a :
		print("Area = {:.1f}".format(A))
else :
		print("Perimetro = {:.1f}".format(p))