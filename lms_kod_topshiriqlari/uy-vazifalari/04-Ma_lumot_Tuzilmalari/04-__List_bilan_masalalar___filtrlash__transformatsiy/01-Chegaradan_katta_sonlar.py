sonlar = list(map(int, input().split()))
t = int(input())

natija = [str(x) for x in sonlar if x > t]
print(" ".join(natija))