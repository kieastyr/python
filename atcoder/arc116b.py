import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
n = int(input())
a = list(map(int, input().split()))
a.sort()
a.insert(0, 0)
ans = 0
sum = 0
for i in range(1, n+1):
    sum *= 2
    sum -= a[i-1]
    sum += a[i]
    sum %= mod
    ans += a[i]*sum
    ans %= mod

print(ans)
