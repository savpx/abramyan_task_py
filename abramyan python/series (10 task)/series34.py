k = int(input())
n = int(input())
for i in range(k):
    s = 0
    has2 = False
    for j in range(n):
        x = int(input())
        s += x
        if x == 2:
            has2 = True
    if has2:
        print(s)
    else:
        print(0)
