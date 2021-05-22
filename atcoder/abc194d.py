import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
ans = 0
for i in range(1, n):
    ans += n/i

print(ans)