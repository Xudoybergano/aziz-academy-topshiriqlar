birinchi = set(input().split())

ikkinchi = input().split()

natija = sum(1 for x in ikkinchi if x in birinchi)

print(natija)