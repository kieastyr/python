import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
k = int(input())
ans = 0

a = 1
while a <= k//a:
    kk = k//a
    b = a
    while b <= kk//b:
        c_max = kk//b
        # print(a,b,c_max)
        if a == b and b == c_max:
            ans += 1
        elif a == b:
            ans += (c_max-b)*3 + 1
        else:
            ans += (c_max-b)*6 + 3
        b += 1
    a += 1

print(ans)




