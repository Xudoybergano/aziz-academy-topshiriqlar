word = input().strip()
unique_chars = {ch for ch in word}
result = list(unique_chars)
result.sort()
print(result)