n = int(input())
groups = {}

for _ in range(n):
    data = input().split()
    groups_name = data[0]
    students = data[1:]
    groups[groups_name] = students
    
for groups_name, students in groups.items():
    print(f"{groups_name} {len(students)}")