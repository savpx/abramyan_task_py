k = int(input())
n = int(input())
found = False
for i in range(n):
    if int(input()) < k:
        found = True
if found:
    print("TRUE")
else:
    print("FALSE")
