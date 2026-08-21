n = int(input())
students = []
total_score = 0

for _ in range(n):
    name, score = input().split()
    score = int(score)
    students.append({"name": name, "score": score})
    total_score += score
    
avg = total_score / n

for student in students:
    if student["score"] > avg:
        print(student["name"])