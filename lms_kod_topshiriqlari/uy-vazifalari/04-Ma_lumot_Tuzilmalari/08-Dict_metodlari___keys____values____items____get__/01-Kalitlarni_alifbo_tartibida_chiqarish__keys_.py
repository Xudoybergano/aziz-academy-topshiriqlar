n = int(input())
d = {}

for _ in range(n):
    ism, baho = input().split()
    d[ism] = int(baho)
    
for ism in sorted(d.keys()):
    print(ism, end=' ')