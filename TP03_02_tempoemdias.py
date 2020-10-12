tempo = int(input())
ano = tempo // 365
mes = (tempo - 365*ano) // 30
dia = (tempo - 365*ano - 30*mes)
print("{:.0f} ano(s)".format(ano))
print("{:.0f} mes(es)".format(mes))
print("{:.0f} dia(s)".format(dia))