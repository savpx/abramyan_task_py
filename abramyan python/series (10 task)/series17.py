b = float(input())
n = int(input())
inserted = False
for i in range(n):
    x = float(input())
    if not inserted and b < x:
        print(b)
        inserted = True
    print(x)
if not inserted:
    print(b)
