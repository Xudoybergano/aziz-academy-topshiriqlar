words = input().split()

result = [w for w in words if len(w) >= 5]

print(result)