s = input().strip()

counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1
    
for char in sorted(counts.keys()):
    print(char, counts[char])