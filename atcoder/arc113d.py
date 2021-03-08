import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
n, m, k = map(int, input().split())

if n == 1 and m == 1:
    print(k)
elif n == 1:
    ans = pow(k, m, mod)
    # yojisho = 0
    # for i in reversed(range(1, k+1)):
    #     i_m = pow(k-i+1, m, mod)
    #     ans = (ans+(pow(k-i+1, m, mod)-yojisho)%mod)%mod
    #     yojisho = i_m
    print(ans)
elif m == 1:
    ans = pow(k, n, mod)
    print(ans)
else:
    ans = 0
    yojisho = 0
    for i in range(1, k+1):
        i_n = pow(i, n, mod)
        ans = (ans+ ((i_n-yojisho)%mod)*pow(k-i+1, m, mod))%mod
        yojisho = i_n
    print(ans)
        