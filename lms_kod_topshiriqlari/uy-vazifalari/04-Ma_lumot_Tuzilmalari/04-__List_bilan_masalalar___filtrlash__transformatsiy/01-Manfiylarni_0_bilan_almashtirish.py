sonlar = list(map(int, input().split()))

natija = [0 if x < 0 else x for x in sonlar]

print(*natija)