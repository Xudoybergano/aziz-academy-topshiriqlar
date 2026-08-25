def daraja(asos, kotarma=2):
    return asos ** kotarma

if __name__ == '__main__':
    asos = int(input())
    kotarma = int(input())
    
    print(daraja(asos))
    print(daraja(asos, kotarma))