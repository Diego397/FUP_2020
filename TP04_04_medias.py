cont = int(input())
for cont in range(0, cont):
		a, b, c = map(float,input().split())
		media = (a*2 + b*3 + c*5)/10
		print("{:.1f}".format(media))