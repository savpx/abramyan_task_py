k = int(input())
count = 0
for i in range(k):
    a = []
    while True:
        x = int(input())
        if x == 0:
            break
        a.append(x)
    ok = True
    for j in range(1, len(a) - 1):
        big = a[j] > a[j - 1] and a[j] > a[j + 1]
        small = a[j] < a[j - 1] and a[j] < a[j + 1]
        if not big and not small:
            ok = False
            break
    if ok:
        count += 1
print(count)
