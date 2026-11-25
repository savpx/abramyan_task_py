k = int(input())
n = int(input())
count = 0
for i in range(k):
    has2 = False
    for j in range(n):
        if int(input()) == 2:
            has2 = True
    if has2:
        count += 1
print(count)
