n = int(input())
students = []

for _ in range(n):
    name, math, phys = input().split()
    students.append({
        "ism": name,
        "mat": int(math),
        "fiz": int(phys)
        
    })
    
for student in students:
    total = student["mat"] + student["fiz"]
    print(f"{student['ism']} {total}")