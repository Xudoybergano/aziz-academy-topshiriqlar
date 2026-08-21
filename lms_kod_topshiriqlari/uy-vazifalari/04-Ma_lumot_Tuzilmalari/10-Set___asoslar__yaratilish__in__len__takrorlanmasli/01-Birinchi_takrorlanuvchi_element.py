numbers = input().split()
seen = set()

found = False
for num in numbers:
    if num in seen:
        print(num)
        found = True
        break
    seen.add(num)
    
if not found:
    print("Yo'q")