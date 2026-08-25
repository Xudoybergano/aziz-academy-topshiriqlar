def raqamlar_yigindisi(n):
    yigindi = 0
    while n > 0:
        yigindi += n % 10
        n //= 10
    return yigindi

if __name__ == '__main__':
    
    n = int(input())
    
    print(raqamlar_yigindisi(n))