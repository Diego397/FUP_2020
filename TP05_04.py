n = [0] * 20
for i in range(19,-1,-1):
		n[i] = int(input())
for i in range(0,20):
		print("N[{:.0f}] = {:.0f}".format(i,n[i]))