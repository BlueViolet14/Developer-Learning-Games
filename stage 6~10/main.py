line = input().strip()
words = line.split()
counts = {} 

for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

for word, count in counts.items():
    print(f"{word}: {count}")