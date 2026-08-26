n = int(input())
lugat = {}

for _ in range(n):
    qator = input().split()
    kalit = qator[0]
    qiymat = qator[1]
    lugat[kalit] = qiymat
    
izlanadigan_kalit = input().strip()
print(lugat.get(izlanadigan_kalit, "Yo'q"))