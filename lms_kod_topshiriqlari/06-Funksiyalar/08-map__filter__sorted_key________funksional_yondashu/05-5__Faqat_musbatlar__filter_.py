nums = list(map(int, input().split()))

musbatlar = list(filter(lambda x: x > 0, nums))

print(*(musbatlar))