n = int(input())
prev = float(input())
result = 0
for i in range(2, n + 1):
    x = float(input())
    if result == 0 and x >= prev:
        result = i
    prev = x
print(result)
