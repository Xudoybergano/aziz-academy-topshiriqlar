n = int(input())

min_son = int(input())

for _ in range(n - 1):
    son = int(input())
    if son < min_son:
        min_son = son
        
print(min_son)