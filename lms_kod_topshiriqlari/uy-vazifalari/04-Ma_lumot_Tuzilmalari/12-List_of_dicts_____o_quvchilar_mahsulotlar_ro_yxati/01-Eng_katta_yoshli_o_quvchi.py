n = int(input())

max_yosh = -1
max_ism = ""

for _ in range(n):
    ism, yosh = input().split()
    yosh = int(yosh)
    
    if yosh > max_yosh:
        max_yosh = yosh
        max_ism = ism
        
print(max_ism)