n = int(input())
total_students = 0

for _ in range(n):
    data = input().split()
    students = data[1:]
    total_students += len(students)
    
print(total_students)