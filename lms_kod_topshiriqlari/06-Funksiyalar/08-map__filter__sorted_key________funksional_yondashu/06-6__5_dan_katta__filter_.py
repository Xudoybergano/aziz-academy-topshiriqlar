nums = list(map(int, input().split()))

katta_besh = list(filter(lambda x: x > 5, nums))

print(*katta_besh)