k = int(input())
count = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x < k:
        count += 1
print(count)
