def rename_keys(prefix='', **kwargs):
    return {prefix + key: value for key, value in kwargs.items()}

prefix = input().strip()
n = int(input())
kwargs = {}

for _ in range(n):
    line = input().split()
    key = line[0]
    value = int(line[1])
    kwargs[key] = value
    
result = rename_keys(prefix, **kwargs)
print(result)