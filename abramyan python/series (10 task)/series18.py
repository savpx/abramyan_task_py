n = int(input())
prev = int(input())
print(prev)
for i in range(1, n):
    x = int(input())
    if x != prev:
        print(x)
    prev = x
