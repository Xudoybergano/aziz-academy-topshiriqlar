n = int(input())

for _ in range(n):
    
    name, price = input().split()
    
    formatted_line = name.ljust(10) + price.rjust(6)
    
    print(formatted_line)