import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

m_fact = {1: 1}
max_fact = 1

def mod_fact(n):
    global max_fact
    if n > max_fact:
        ans = m_fact[max_fact]
        start = max_fact+1
    else:
        ans = 1
        start = 2
    for i in range(start, n+1):
        ans *= i
        ans %= mod
    max_fact = n
    m_fact[n] = ans
    return ans

n = int(input())
a_sort = sorted(list(map(int, input().split())), reverse=True)
d = []
for i in range(1, n):
    if a_sort[i-1]-a_sort[i] > 0:
        d.append(a_sort[i-1]-a_sort[i])
d.append(a_sort[-1])
d.sort()
# print(d)
# print(a_sort)
ans = 1
for dd in d:
    ans *= dd+1
    ans %= mod

print(ans)
