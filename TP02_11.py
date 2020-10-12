a, b = map(int,input().split())
if a == b :
		print("O JOGO DUROU 24 HORA(S)")
if a < b :
		print("O JOGO DUROU {:.0f} HORA(S)".format(b-a))
if a > b :
		print("O JOGO DUROU {:.0f} HORA(S)".format(24 - a + b))