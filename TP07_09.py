while True:
    n = int(input())
    if n == 0:
        break
    m = len(str(2 ** (2 * n - 2)))
    for i in range(n):
        for j in range(n):
            print(("{}".format(2 ** (i + j))).rjust(m), end = " " if j != n - 1 else "")
        print("")
    print("")