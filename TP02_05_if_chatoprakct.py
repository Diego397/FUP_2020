a, b, c, d = map(float,input().split())
if a >= 0 and b >= 0 and c >= 0 and d >= 0 :
		media = (a*2 + b*3 + c*4 + d*1)/10
		print("Media: {:.1f}".format(media))
		if media >= 7 :
				print("Aluno aprovado.")
		if 0 <= media < 5 :
				print("Aluno reprovado.")
		if 5 <= media < 7 :
				print("Aluno em exame.")
				e = float(input())
				print("Nota do exame: {:.1f}".format(e))
				if e >= 5 :
						mediaf = (media + e)/2
						print("Aluno aprovado.")
						print("Media final: {:.1f}".format(mediaf))
				if e >= 0 and e < 5 :
						print("Aluno reprovado.")
						print("Media final: {:.1f}".format(media))