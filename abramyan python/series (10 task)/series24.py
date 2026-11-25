n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
last = -1
prev = -1
for i in range(n):
    if a[i] == 0:
        prev = last
        last = i
s = 0
for i in range(prev + 1, last):
    s += a[i]
print(s)
