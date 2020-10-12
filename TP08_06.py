p, j1, j2, r, a = map(int,input().split())
s = j1 + j2
resto = s % 2
if r == 1 and a == 0:
		vencedor = 1
elif r == 0 and resto != p:
		vencedor = 1
else:
		vencedor = 2
print("Jogador {} ganha!".format(vencedor))