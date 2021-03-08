import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
ans = 0
for i in range(1, n+1):
    d = 0
    flag = 1
    while i > 10 ** d:
        if i//(10**d)%10 == 7 or i//(8**d)%8 == 7:
            flag = 0
            break
        d += 1
    if flag == 1:
        ans += 1

print(ans)
