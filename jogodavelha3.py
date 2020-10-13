#Diego Alejandro Balejo Cardozo Rey 495908
m = [[" "]*3 for i in range(3)] #definir derivaveis
cont = 1
emp = 0
vit1 = 0
vit2 = 0
def adversario(x): #função para determinar o simbolo do jogador adversario
	return "O" if x == "X" else "X"
def tabela(x): #função que mostra a tabela do jogo da velha
	t = "   A   B   C\n1  {} | {} | {}  1\n  ---+---+---\n2  {} | {} | {}  2\n  ---+---+---\n3  {} | {} | {}  3\n   A   B   C".format(x[0][0], x[0][1], x[0][2], x[1][0], x[1][1], x[1][2], x[2][0], x[2][1], x[2][2])
	print(t)
def testa_vitoria(x): #função que testa se o jogador da vez ganhou a partida, verifica se existem 3 simbolos iguais em uma mesma coluna, linha ou diagonal
	diagonal1 = [x[i][i] for i in range(3)]
	diagonal2 = [x[i][2 - i] for i in range(3)]
	for i in range(3):
		linhas = [x[i][j] for j in range(3)]
		colunas = [x[j][i] for j in range(3)]
		if linhas.count("X") == 3 or colunas.count("X") == 3:
			return "X"
		if linhas.count("O") == 3 or colunas.count("O") == 3:
			return "O"
	if diagonal1.count("X") == 3 or diagonal2.count("X") == 3:
		return "X"
	if diagonal1.count("O") == 3 or diagonal2.count("O") == 3:
		return "O"
	return " "
def consegue_ganhar(x, y): #função que verifica se o jogador consegue ganhar, 
	for i in range(3):
		for j in range(3):
			if x[i][j] in ["", " "]:
				x[i][j] = y
				if testa_vitoria(x) == y:
					x[i][j] = " "
					return True
				x[i][j] = " "
	return False
def ja_perdeu(x, y): #função que verifica se o jogador perdeu independente de onde ele coloque na próxima jogada
	for i in range(3):
		for j in range(3):
			if x[i][j] in ["", " "]:
				x[i][j] = y 
				if not consegue_ganhar(x, adversario(y)) or testa_vitoria(x) == y:
					x[i][j] = " "
					return False
				x[i][j] = " "

	return True
while True: #laço que para quando os jogadores não querem mais jogar
	while True: #laço que para quando o jogador 1 escolher um simbolo adequado
		simbolo1 = str(input("Simbolo do jogador 1 = "))
		if simbolo1 == "X":
			simbolo2 = "O"
			break
		if simbolo1 == "O":
			simbolo2 = "X"
			break
	cont = 1
	m = [[" "]*3 for i in range(3)]
	while cont < 10: #laço que conta o número de jogadas e para quando um jogador vence ou quando da empate
		rcont = cont % 2
		if rcont == 0:
			jogador = 2
			simbolo = simbolo2
			jogadoradv = 1
			simboloadv = simbolo1
		else:
			jogador = 1
			simbolo = simbolo1
			jogadoradv = 2
			simboloadv = simbolo2
		while True: #laço para receber as coordenadas do lugar onde o jogador escolher, ele só recebe quando a entrada for válida
			tabela(m)
			coords = (str(input("Vez do jogador {} = ".format(jogador))))
			l = "".join((ch if ch in "123.-e" else "") for ch in coords)	#l é a parte númerica das coordenadas, só é validada para l = 1, 2 ou 3
			c = "".join((s if s in "aAbBcC.-e" else "")for s in coords)	#c é o caractere das coordenadas, só é validada para c = a, A, b, B, c ou C
			if l == "1" or l == "2" or l == "3":
				l = (int(l) - 1)
			else:
				l = 9
			if c == "a" or c == "A":
				c = 0
			elif c == "b" or c == "B":
				c = 1
			elif c == "c" or c == "C":
				c = 2
			else:
				c = 9
			if 0 <= l <= 2 and 0 <= c <= 2 and m[l][c] == " ": #se l e c estiverem dentro do intervalo aceito e a coordenada escolhida não estiver preenchida, a coordenada é validada e registrada
				m[l][c] = simbolo
				cont = cont + 1 #contador de jogadas validas
				break
			else:
				print("Entrada invalida")
		flag = 0 #bandeira para saber se o jogador venceu
		if (ja_perdeu(m,simboloadv) and consegue_ganhar(m,simbolo)) or testa_vitoria(m) == simbolo: #se o adversario já perdeu a partida e o jogador da vez conseguir ganhar ou o jogador da vez ganhar, o jogador da vez ganha
			if testa_vitoria(m) == simbolo:
				tabela(m)
				print("jogador {} venceu".format(jogador))
			else:
				tabela(m)
				print("Jogador {} venceu antes mesmo do jogador {} jogar".format(jogador,jogadoradv))
			if jogador == 1: #condição para adicionar ao contador de vitoria
				vit1 = vit1 + 1
			else:
				vit2 = vit2 + 1
			flag = 1
			cont = 10
			break
		if cont == 10 and flag == 0: #se nenhum jogador tiver vencido e ja foram realizadas 9 jogadas, da empate
			tabela(m)
			print("O jogo deu empate")
			emp = emp + 1
			break
	print("O jogador 1 tem {} vitoria(s), o Jogador 2 tem {} vitoria(s) e houve(ram) {} empate(s)".format(vit1,vit2,emp)) #formato dos resultados de todas as patidas jogadas até o momento
	resposta = str(input('Jogar denovo? (Se sim, digite "sim") ')) #pergunta ao usuario se ele quer jogar novamente
	if resposta != "sim": #se o usuario quiser jogar novamente, deve digitar "sim"
		break
	else:
		print("Jogo reiniciado")
