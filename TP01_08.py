x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
d1 = (x2-x1)
d2 = (y2-y1)
D = ( d1**2 + d2**2)**(1/2) 
print("{:.4f}".format(D))