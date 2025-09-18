n = int(input())
total = 0

for i in range(n):
    i += 1
    if i % 2 == 0:
        total += i

print("EVEN SUM:", total)