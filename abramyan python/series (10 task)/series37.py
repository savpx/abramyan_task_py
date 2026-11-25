k = int(input())
count = 0
for i in range(k):
    prev = int(input())
    incr = True
    decr = True
    while True:
        x = int(input())
        if x == 0:
            break
        if x <= prev:
            incr = False
        if x >= prev:
            decr = False
        prev = x
    if incr or decr:
        count += 1
print(count)
