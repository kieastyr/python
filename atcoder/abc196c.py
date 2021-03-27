import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
n_copy = n
ans = 0

i = 0
while n_copy >= 100:
    n_copy //= 100
    ans += 9*(10**i)
    i += 1

if n_copy >= 10:
    n1 = n//(10**(i+1))
    n2 = n%(10**(i+1))
    if n1 <= n2:
        ans += n1-10**i+1
    else:
        ans += n1-10**i

print(ans)

