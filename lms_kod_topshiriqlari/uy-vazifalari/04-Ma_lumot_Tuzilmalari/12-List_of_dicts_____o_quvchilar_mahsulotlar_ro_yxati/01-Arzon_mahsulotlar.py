n = int(input())

mahsulotlar = []

for _ in range(n):
    qator = input().split()
    nomi = qator[0]
    narxi = int(qator[1])
    
    mahsulot = {"nomi": nomi, "narxi": narxi}
    mahsulotlar.append(mahsulot)
    
chegara = int(input())

for m in mahsulotlar:
    if m["narxi"] < chegara:
        print(m["nomi"])