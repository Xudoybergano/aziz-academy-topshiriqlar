words = input().split()

unique_lengths = {len(w) for w in words}

result = list(unique_lengths)
result.sort()

print(result)