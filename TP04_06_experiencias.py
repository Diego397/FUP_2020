cont = int(input())
soma = 0
nc = 0 
nr = 0
ns = 0
for cont in range(0, cont):
		n, animal = map(str,input().split())
		n = int(n)
		soma = soma + n
		if animal == "C":
				nc = nc + n
		elif animal == "R":
				nr = nr + n
		else:
				ns = ns + n
pc = (nc / soma) * 100
pr = (nr / soma) * 100
ps = (ns / soma) * 100
print("Total: {:.0f} cobaias".format(soma))
print("Total de coelhos: {:.0f}".format(nc))
print("Total de ratos: {:.0f}".format(nr))
print("Total de sapos: {:.0f}".format(ns))
print("Percentual de coelhos: {:.2f} %".format(pc))
print("Percentual de ratos: {:.2f} %".format(pr))
print("Percentual de sapos: {:.2f} %".format(ps))