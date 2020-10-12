a, b, c= map(int,input().split())
m1 = (a + b + abs(a-b))/2
m2 = int((c + m1 + abs(c-m1))/2)
print(m2,"eh o maior")