total = {}

n = int(input())
for _ in range(n):
    item, qty = input().split()
    total[item] = total.get(item, 0) + int(qty)
    
m = int(input())
for _ in range(m):
    item, qty = input().split()
    total[item] = total.get(item, 0) + int(qty)
    
for item in sorted(total.keys()):
    print(f"{item} {total[item]}")