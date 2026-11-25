n = int(input())
prev = float(input())
ok = True
for i in range(1, n):
    x = float(input())
    if x <= prev:
        ok = False
    prev = x
if ok:
    print("TRUE")
else:
    print("FALSE")
