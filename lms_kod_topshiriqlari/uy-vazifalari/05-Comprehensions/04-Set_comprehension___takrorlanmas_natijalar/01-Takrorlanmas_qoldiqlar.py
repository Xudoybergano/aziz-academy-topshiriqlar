nums = [int(x) for x in input().split()]

unique_remainsers = {x % 3 for x in nums}

result = list(unique_remainsers)
result.sort()

print(result)