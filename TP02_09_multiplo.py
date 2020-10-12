a, b = map(int,input().split())
resto1 = a % b
resto2 = b % a
if resto1 == 0 or resto2 == 0 :
		print("Sao Multiplos")
else :
		print("Nao sao Multiplos")