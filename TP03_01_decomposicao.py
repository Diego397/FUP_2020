a = int(input())
v1 = a // 100
v2 = (a - (v1*100)) // 50
v3 = (a - (v1*100 + v2*50)) // 20
v4 = (a - (v1*100 + v2*50 + v3*20)) // 10
v5 = (a - (v1*100 + v2*50 + v3*20 + v4*10)) // 5
v6 = (a - (v1*100 + v2*50 + v3*20 + v4*10 + v5*5)) // 2
v7 = (a - (v1*100 + v2*50 + v3*20 + v4*10 + v5*5 + v6*2)) // 1
print(a)
print("{:.0f} nota(s) de R$ 100,00".format(v1))
print("{:.0f} nota(s) de R$ 50,00".format(v2))
print("{:.0f} nota(s) de R$ 20,00".format(v3))
print("{:.0f} nota(s) de R$ 10,00".format(v4))
print("{:.0f} nota(s) de R$ 5,00".format(v5))
print("{:.0f} nota(s) de R$ 2,00".format(v6))
print("{:.0f} nota(s) de R$ 1,00".format(v7))