elements = input().split()

counts = {}
for item in elements:
    counts[item] = counts.get(item, 0) + 1
    
max_element = max(elements, key=lambda x: counts[x])

print(max_element)