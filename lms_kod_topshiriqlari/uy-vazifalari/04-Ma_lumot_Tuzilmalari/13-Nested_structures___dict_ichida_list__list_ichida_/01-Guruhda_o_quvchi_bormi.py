n = int(input())
groups = {}

for _ in range(n):
    data = input().split()
    groups_name = data[0]
    students = data[1:]
    groups[groups_name] = students
    
target_groups, target_student = input().split()

if target_student in groups[target_groups]:
    print("Ha")
else:
    print("Yoq")