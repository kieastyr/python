import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, m, q = map(int,input().split())
wv = {}
for i in range(1, n+1):
    w, v = list(map(int,input().split()))
    wv[i] = [-w, v]
wv_s = sorted(wv.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)

x = {i: num for i, num in zip(range(1, m+1), list(map(int,input().split())))}
x_s = sorted(x.items(), key=lambda x: x[1])
# print(wv_s)

for _ in range(q):
    l, r = map(int,input().split())
    ans = 0
    use = [0]*(m+1)
    for i in range(n):
        w, v = wv_s[i][1]
        j = 1
        while j < m+1 and (use[j]==1 or l <= x_s[j-1][0] <= r or x_s[j-1][1] < -w):
            j += 1
        if j < m+1:
            ans += v
            use[j] = 1
            # print(wv_s[i][0], x_s[j-1][0])
    
    print(ans)
    # del use

