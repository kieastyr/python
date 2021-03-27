import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
# n = 2*10**5
f = list(map(int,input().split()))
# f = [i for i in range(1, n+1)]
f.insert(0, 0)
totta = [0 for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    if totta[i] == 0:
        root = []
        while totta[i] == 0:
            root.append(i)
            totta[i] = 1
            i = f[i]
        if i in root:
            ans += 1
        del root


print((pow(2, ans, mod)-1)%mod)
