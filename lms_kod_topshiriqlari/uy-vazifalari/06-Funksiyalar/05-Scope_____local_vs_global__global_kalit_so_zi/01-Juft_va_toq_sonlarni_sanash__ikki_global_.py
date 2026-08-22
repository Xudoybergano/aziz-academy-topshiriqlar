juft = 0
toq = 0


def sanash(x):
    global juft, toq
    if x % 2 == 0:
        juft += 1
    else:
        toq += 1


sonlar = map(int, input().split())
for son in sonlar:
    sanash(son)

print(f"{juft} {toq}")