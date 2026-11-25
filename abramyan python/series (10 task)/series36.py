k = int(input())
count = 0
for i in range(k):
    prev = int(input())
    incr = True
    while True:
        x = int(input())
        if x == 0:
            break
        if x <= prev:
            incr = False
        prev = x
    if incr:
        count += 1
print(count)
