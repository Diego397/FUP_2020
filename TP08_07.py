a, b, c = map(int,input().split())
if a > b and c >= b:
		print(":)")
elif b > a and b >= c:
		print(":(")
elif b > a and c > b and abs(c-b) < abs(b-a):
		print(":(")
elif b > a and c > b and abs(c-b) >= abs(b-a):
		print(":)")
elif a > b and b > c and abs(b-c) < abs(a-b):
		print(":)")
elif a > b and b > c and abs(b-c) >= abs(a-b):
		print(":(")
elif a == b and c > b:
		print(":)")
elif a == b and b > c:
		print(":(")
elif a == b == c:
		print(":(")