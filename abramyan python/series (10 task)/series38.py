k = int(input())
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
    if incr:
        print(1)
    elif decr:
        print(-1)
    else:
        print(0)
