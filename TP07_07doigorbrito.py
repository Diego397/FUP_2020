while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        for j in range(n):
            print("{:3}".format(min(i + 1, j + 1, n - i, n - j)), end = " " if j != n - 1 else "")
        print("")
    print("")