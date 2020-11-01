num = list(map(int, input().split()))
ans = 0

for i in range(8):
    a = 0
    b = 0
    for j in range(4):
        if (i >> j) & 1 == 1:
            a += num[j]
        else:
            b += num[j]
    if a == b:
        ans = 1

if ans == 1:
    print("Yes")
else:
    print("No")       
