def narxi_bilan(narx, soliq=12):
    return narx + narx * soliq // 100

narx = int(input())
soliq = int(input())

print(narxi_bilan(narx))
print(narxi_bilan(narx, soliq))