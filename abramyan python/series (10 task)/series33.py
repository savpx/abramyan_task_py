k = int(input())
n = int(input())
for i in range(k):
    result = 0
    for j in range(n):
        x = int(input())
        if x == 2:
            result = j + 1
    print(result)
