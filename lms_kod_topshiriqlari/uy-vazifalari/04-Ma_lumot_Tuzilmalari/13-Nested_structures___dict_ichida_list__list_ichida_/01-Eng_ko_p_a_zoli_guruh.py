n = int(input())
groups = {}

for _ in range(n):
    data = input().split()
    group_name = data[0]
    members = data[1:]
    groups[group_name] = members
    
max_group = None
max_count = -1

for group_name, members in groups.items():
    if len(members) > max_count:
        max_count = len(members)
        max_group = group_name
        
print(max_group)