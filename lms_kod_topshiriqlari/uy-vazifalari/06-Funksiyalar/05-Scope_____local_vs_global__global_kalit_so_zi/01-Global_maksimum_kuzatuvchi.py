eng_katta = None


def tekshir(x):
    global eng_katta
    if x > eng_katta:
        eng_katta = x


sonlar = list(map(int, input().split()))

if sonlar:
    eng_katta = sonlar[0]
    for son in sonlar[1:]:
        tekshir(son)

    print(eng_katta)