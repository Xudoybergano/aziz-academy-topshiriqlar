transport = int(input())
toifa = int(input())

# Transport narxini aniqlash
if transport == 1:
    narx = 1700
elif transport == 2:
    narx = 1700
elif transport == 3:
    narx = 4000
else:
    print("Notogri transport")
    exit()
    
# Yo'lovchi toifasi va chegirani hisoblash
if toifa == 1:
    print(narx)
elif toifa == 2:
    print(narx // 2)
elif toifa == 3:
    print(0)
else:
    print("Notogri toifa")