import sys
import math

def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

n = int(input())
s = list(map(int, list(input())))
t = list(map(int, list(input())))

to0 = []
to1 = []
ans = 0

for i in range(n):
    if s[i]-t[i] > 0:
        if len(to1) == 0:
            to0.append(i)
        else:
            to1.pop(-1)
    if s[i] == 0 and (len(to0) > 0 or len(to1) > 0):
        ans += 1
    
    if s[i]-t[i] < 0:
        if len(to0) == 0:
            if len(to1) == 0:
                ans += 1
            to1.append(i)
        else:
            to0.pop(-1)
    # print(f'{i}: {ans}')

if (len(to0) == 0 and len(to1) == 0):
    print(ans)
else:
    print(-1)
