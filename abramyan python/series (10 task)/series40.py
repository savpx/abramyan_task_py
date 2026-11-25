k = int(input())
for i in range(k):
    a = []
    while True:
        x = int(input())
        if x == 0:
            break
        a.append(x)
    result = 0
    for j in range(1, len(a) - 1):
        big = a[j] > a[j - 1] and a[j] > a[j + 1]
        small = a[j] < a[j - 1] and a[j] < a[j + 1]
        if not big and not small:
            result = j + 1
            break
    if result == 0:
        print(len(a))
    else:
        print(result)
