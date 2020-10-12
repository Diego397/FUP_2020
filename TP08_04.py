while True:
		x0, y0, x1, y1 = map(int,input().split())
		if x0 == y0 == x1 == y1 == 0:
				break
		elif x0 == x1 and y0 == y1:
				m = 0
		elif x0 == x1 or y0 == y1 or abs(x0 - x1) == abs(y0 - y1):
				m = 1
		else:
				m = 2	
		print(m)