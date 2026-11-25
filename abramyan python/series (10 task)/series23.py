n = int(input())
a = []
for i in range(n):
    a.append(float(input()))
result = 0
for i in range(1, n - 1):
    big = a[i] > a[i - 1] and a[i] > a[i + 1]
    small = a[i] < a[i - 1] and a[i] < a[i + 1]
    if not big and not small:
        result = i + 1
        break
print(result)
