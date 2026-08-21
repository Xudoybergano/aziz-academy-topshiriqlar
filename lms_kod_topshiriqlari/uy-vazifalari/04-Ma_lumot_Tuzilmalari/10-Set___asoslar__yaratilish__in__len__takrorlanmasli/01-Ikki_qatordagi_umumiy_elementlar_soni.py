set1 = set(input().split())
set2 = set(input().split())

common = set1.intersection(set2)
print(len(common))