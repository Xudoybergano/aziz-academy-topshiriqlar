n = int(input())

a, b = 0, 1
natija = []

for _ in range(n):
    natija.append(str(a))
    a, b = b, a + b
    
print(" ".join(natija))