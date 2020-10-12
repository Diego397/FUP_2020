cont = int(input())
soma = 0
for cont in range(0,cont):
		soma = 0
		x,y = map(int,input().split())
		if x > y:
				i = x - y
				for i in range(1,i):
						n1 = y + i
						resto = n1 % 2
						if resto == 0:
								soma = soma
						else:
								soma = soma + n1
		else:
				i = y - x
				for i in range(1,i):
						n1 = x + i
						resto = n1 % 2
						if resto == 0:
								soma = soma
						else:
								soma = soma + n1
		print(soma)