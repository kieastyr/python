import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
num = n
c = 0
ans = 0
while num >= 1000:
    num //= 1000
    ans += c*999*1000**c
    c += 1

# print(ans)

minus = 0
for i in range(c):
    minus += 999*1000**i

ans += c*(n-minus)
print(ans)
 
