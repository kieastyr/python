import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
s = list(map(int, list(input())))
x = list(input())

dp = [set() for _ in range(n+1)]
dp[n].add(0)

for i in range(n-1, -1, -1):
    if x[i] == 'T':
        for r in range(7):
            if 10*r%7 in dp[i+1]:
                dp[i].add(r)
            if (10*r+s[i])%7 in dp[i+1]:
                dp[i].add(r)
    else:
        for r in range(7):
            if 10*r%7 in dp[i+1] and (10*r+s[i])%7 in dp[i+1]:
                dp[i].add(r)
    # print(x[i], s[i], dp[i])

if 0 in dp[0]:
    print("Takahashi")
else:
    print("Aoki")