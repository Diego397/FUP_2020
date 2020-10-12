di = int(input().split()[1])
hi, mi, si = map(int,input().split(" : "))
df = int(input().split()[1])
hf, mf, sf = map(int,input().split(" : "))
tempoi = di * (24 * 60 * 60) + hi * (60 * 60) + mi * 60 + si
tempof = df * (24 * 60 * 60) + hf * (60 * 60) + mf * 60 + sf
dif = tempof - tempoi
dia = dif // (24 * 60 * 60)
hora = (dif - (dia * (24 * 60 * 60))) // (60 * 60)
minu = (dif - (dia * (24 * 60 * 60) + hora * 60 * 60)) // 60
sec = dif - (dia * (24 * 60 * 60) + hora * 60 * 60 + minu * 60)
print("{:.0f} dia(s)".format(dia))
print("{:.0f} hora(s)".format(hora))
print("{:.0f} minuto(s)".format(minu))
print("{:.0f} segundo(s)".format(sec))