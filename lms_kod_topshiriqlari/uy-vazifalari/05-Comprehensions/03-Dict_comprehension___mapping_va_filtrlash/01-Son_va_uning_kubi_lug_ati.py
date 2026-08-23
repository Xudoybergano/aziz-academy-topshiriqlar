nums = [int(x) for x in input().split()]

result = {x: x * x * x for x in nums}
print(result)