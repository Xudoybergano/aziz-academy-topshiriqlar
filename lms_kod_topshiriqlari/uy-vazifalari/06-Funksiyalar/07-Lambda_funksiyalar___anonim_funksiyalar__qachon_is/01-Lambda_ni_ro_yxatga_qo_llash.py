f = lambda x: x * x + 1
sonlar = map(int, input().split())
natijalar = map(str, map(f, sonlar))
print(" ".join(natijalar))