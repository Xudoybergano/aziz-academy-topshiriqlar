sonlar = set(map(int, input().split()))

qidiriluvchi = int(input())

if qidiriluvchi in sonlar:
    print("Bor")
else:
    print("Yo'q")