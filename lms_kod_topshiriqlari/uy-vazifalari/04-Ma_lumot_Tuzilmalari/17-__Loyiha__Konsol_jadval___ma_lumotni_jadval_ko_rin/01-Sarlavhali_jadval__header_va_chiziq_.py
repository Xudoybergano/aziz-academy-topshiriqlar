n = int(input())

print("Mahsulot".ljust(10) + "Soni".rjust(6))

print("-" * 16)

for _ in range(n):
    name, count = input().split()
    print(name.ljust(10) + count.rjust(6))