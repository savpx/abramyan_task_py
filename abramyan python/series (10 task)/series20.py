n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = 0
for i in range(n - 1):
    if a[i] < a[i + 1]:
        print(a[i])
        k += 1
print(k)
