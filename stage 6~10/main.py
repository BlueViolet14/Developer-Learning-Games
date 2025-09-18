a, b = map(int, input().split())
s = a + b
diff = a - b
prod = a * b
quod = a // b if b != 0 else "DIV0"
rem = a % b if b != 0 else "DIV0"

print("SUM:", s)
print("DIFF:", diff)
print("PROD:", prod)
print("QUOT:", quod)
print("REM:", rem)