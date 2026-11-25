k = int(input())
i = 0
result = 0
while True:
    x = int(input())
    if x == 0:
        break
    i += 1
    if result == 0 and x > k:
        result = i
print(result)
