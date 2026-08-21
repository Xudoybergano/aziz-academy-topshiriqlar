n = int(input())
d = {}

for _ in range(n):
    item, count = input().split()
    d[item] = count
    
search_item = input()
print(d.get(search_item, "Topilmadi"))