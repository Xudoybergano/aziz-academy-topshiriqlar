def malumot(**kwargs):
    natija = []
    for k, v in kwargs.items():
        natija.append(f"{k}: {v}")
    return natija
                
                
n = int(input())
lugat = {}
for _ in range(n):
  qator = input().split("=")
  lugat[qator[0]] = qator[1]
                
for qator in malumot(**lugat):
   print(qator)