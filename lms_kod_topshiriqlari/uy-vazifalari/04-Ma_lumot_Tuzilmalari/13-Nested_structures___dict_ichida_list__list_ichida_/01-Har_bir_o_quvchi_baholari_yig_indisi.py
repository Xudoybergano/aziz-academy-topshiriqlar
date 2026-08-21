n = int(input())
students = []

for _ in range(n):
    data = input().split()
    name = data[0]
    scores = [int(x) for x in data[1:]]
    students.append({"ism": name, "baholar": scores})
    
for student in students:
    total = sum(student["baholar"])
    print(f"{student['ism']} {total}")