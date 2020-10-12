a = [0] * 100
for i in range(0,100):
		a[i] = float(input())
for i in range(0,100):
		if a[i] <= 10:
				print("A[{:.0f}] = {:.1f}".format(i,a[i]))