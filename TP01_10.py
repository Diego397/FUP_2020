m = 1
n = 1
p = 1
while m != 0 and n != 0 and p != 0:
        m, n, p = map(int,input().split())
        l = 0
        lista = []
        i = int()
        for i in range (0,p):
                lista.append(input())

        contador = int()
        L = 0
        for contador in range (0,len(lista)):
                lista[contador] = int(lista[contador])
                if(lista[contador] > n):
                        contador == 900
                        m = 0
                L = (L + n + 1 - lista[contador])
        if(m > 0):
                print("Lights:",L)