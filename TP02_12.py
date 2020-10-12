h1, m1, h2, m2 = map(int,input().split())
minutosi = h1*60 + m1
minutosf = h2*60 + m2
if (minutosf <= minutosi) :
		minutosf = minutosf + 24*60
minutosd = minutosf - minutosi
print("O JOGO DUROU {:.0f} HORA(S) E {:.0f} MINUTO(S)".format(int(minutosd/60),minutosd%60))