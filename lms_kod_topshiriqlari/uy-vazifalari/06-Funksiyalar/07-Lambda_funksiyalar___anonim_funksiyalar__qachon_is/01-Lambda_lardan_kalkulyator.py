qator = input().split()
a = int(qator[0])
amal = qator[1]
b = int(qator[2])

amallar = {
        "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}

print(amallar[amal](a, b))