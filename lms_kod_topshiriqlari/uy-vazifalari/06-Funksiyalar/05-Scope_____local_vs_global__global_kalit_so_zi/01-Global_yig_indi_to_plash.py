jami = 0

def qosh(x):
    global jami
    jami += x
    
if __name__ == '__main__':
    
    sonlar = map(int, input().split())
    
for son in sonlar:
    
    qosh(son)
        
print(jami)