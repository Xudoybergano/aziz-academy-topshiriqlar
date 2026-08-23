yigindi = 0

while True:
    qator = input().strip()
    
    if qator == "stop":
        break
        
    yigindi += int(qator)
    
print(yigindi)