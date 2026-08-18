def config_get(key, defult=None, **kwargs):
    if key in kwargs:
        return kwargs[key]
    return defult

izlanayotgan = input().strip()
n = int(input())
data = {}
for i in range(n):
    qator = input().split()
    data[qator[0]] = int(qator[1])
    
print(config_get(izlanayotgan, defult=0, **data))