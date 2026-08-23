nums = list(map(int, input().split()))

toq_sonlar = list(filter(lambda x: x % 2 != 0, nums))

print(*(toq_sonlar))