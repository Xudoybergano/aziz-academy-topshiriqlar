nums = [int(x) for x in input().split()]

result = {x: x * x for x in nums if x % 2 == 0}

print(result)