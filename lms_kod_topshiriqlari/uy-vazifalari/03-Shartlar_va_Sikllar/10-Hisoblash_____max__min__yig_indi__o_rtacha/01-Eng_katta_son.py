n = int(input())

max_son = int(input())

for _ in range(n - 1):
    son = int(input())
    if son > max_son:
        max_son = son
        
print(max_son)