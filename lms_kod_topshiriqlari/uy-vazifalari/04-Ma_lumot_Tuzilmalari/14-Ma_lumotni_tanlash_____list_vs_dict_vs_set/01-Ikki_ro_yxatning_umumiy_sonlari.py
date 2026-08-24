set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

common = set1 & set2

print(*(sorted(common)))