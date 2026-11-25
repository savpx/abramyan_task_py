s = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x > 0 and x % 2 == 0:
        s += x
print(s)
