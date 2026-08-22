def kub(x):
    return x * x * x


def yigindi_kublari(n):
    yigindi = 0
    for i in range(1, n + 1):
        yigindi += kub(i)
    return yigindi
                 
                 
n = int(input())
print(yigindi_kublari(n))