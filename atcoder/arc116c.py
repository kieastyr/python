import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

def soinsu(num):
    i = 2
    ans = 0
    num_copy = num
    while num_copy > 1 and i*i <= num:
        while num_copy%i == 0:
            num_copy //= i
            ans += 1
        i += 1
    if ans == 0:
        ans = 1
    elif num_copy != 1:
        ans += 1
    return ans

n, m = map(int, input().split())
waru_m = [0, m-1]
d = 2
m_num = {}
while m//d > 1:
    waru_m.append(m//d-1)
    sd = soinsu(d)
    print(f"{d}:{sd}")
    if m_num.get(sd):
        m_num[sd] += waru_m[-1]
    else:
        m_num[sd] = waru_m[-1]
    d += 1

print(waru_m)

k = max(m_num.keys())
kosu = {k: m_num[k]}
for i in reversed(range(1, k)):
    if m_num.get(i):
        kosu[i] = m_num[i]+kosu[i+1]
    else:
        kosu[i] = kosu[i+1]

print(kosu)

ans = 1
nck = 1
for j in range(1, n+1):
    nck *= (n-j+1)
    nck //= j
    print(n, j, nck)
    if j == 1:
        ans += (m-1)*nck
    elif j-1 > k:
        break
    else:
        ans += kosu[j-1]*nck

print(ans)

