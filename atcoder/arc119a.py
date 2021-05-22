import sys
import math

def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

n = int(input())
ans = 1e18
b = 0
while 2**b <= n:
    a = n//(2**b)
    c = n-a*2**b
    ans = min(ans, a+b+c)
    b += 1

print(ans)
