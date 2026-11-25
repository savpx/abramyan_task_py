k = int(input())
total = 0
for i in range(k):
    count = 0
    while True:
        x = int(input())
        if x == 0:
            break
        count += 1
    print(count)
    total += count
print(total)
