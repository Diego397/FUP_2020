#b = numero de bancos, n = numero de debentures emitidas pelos bancos, d = banco devedor, c = banco credor, v = valor da debenture
while True:
		b, n = map(int,input().split())
		if b == 0 and n == 0:
				break
		reserva = input().split()
		bdev = [0]*n
		bcred = [0]*n
		vdeb = [0]*n
		for i in range(len(reserva)):
				reserva[i] = int(reserva[i])
		for i2 in range(n):
				d, c, v = map(int,input().split())
				bdev[i2] = d
				bcred[i2] = c
				vdeb[i2] = v
		if sum(reserva)*2 >= sum(vdeb):
				print("S")
		else:
				print("N")