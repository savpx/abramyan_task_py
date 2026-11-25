n = int(input())
prev = int(input())
k = 0
for i in range(1, n):
    x = int(input())
    if x < prev:
        print(x)
        k += 1
    prev = x
print(k)
