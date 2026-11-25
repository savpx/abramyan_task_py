n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
first = -1
last = -1
for i in range(n):
    if a[i] == 0:
        if first == -1:
            first = i
        last = i
s = 0
for i in range(first + 1, last):
    s += a[i]
print(s)
