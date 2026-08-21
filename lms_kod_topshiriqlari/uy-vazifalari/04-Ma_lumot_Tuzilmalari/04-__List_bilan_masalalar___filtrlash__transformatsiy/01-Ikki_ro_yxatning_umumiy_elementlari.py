a = input().split()
b = set(input().split())

result = []
for x in a:
    if x in b and x not in result:
        result.append(x)
        
print(*result)