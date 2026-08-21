n = int(input())
names = [input().strip() for _ in range(n)]

max_len = max(len(name) for name in names)

for name in names:
    print(f"{name.ljust(max_len)}|")