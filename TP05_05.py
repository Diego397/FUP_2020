cont = int(input())
for cont in range(0,cont):
        n = int(input())
        fib = [1] * 2
        if n > 1:
                fib = [1] * (n+1)
        fib[0] = 0
        fib[1] = 1
        if n > 2:
                for i in range(2,n+1):
                        fib[i] = fib[i-1] + fib[i-2]
        print("Fib({:.0f}) = {:.0f}".format(n,fib[n]))
        print(fib)