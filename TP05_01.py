lista = [0] * 100
for i in range(0,100):
		lista[i] = int(input())
print(max(lista))
print(lista.index(max(lista)) + 1)