import sys
from collections import Counter

words = sys.stdin.read().split()

counts = Counter(words)

for word in sorted(counts):
    print(f"{word} {counts[word]}")