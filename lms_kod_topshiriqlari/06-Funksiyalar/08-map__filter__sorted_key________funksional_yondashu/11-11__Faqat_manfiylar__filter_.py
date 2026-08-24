nums = list(map(int, input().split()))

manfiylar = list(filter(lambda x: x < 0, nums))

print(*manfiylar)