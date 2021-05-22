import sys
import math
from collections import Counter

def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a = Counter(list(map(int, input().split())))
b = {k: v for k, v in enumerate(list(map(int, input().split())))}
c = Counter(list(map(lambda x: int(x)-1, input().split())))

a_sort = sorted(a.items(), key=lambda x: x[0])
b_sort = sorted(b.items(), key=lambda x: x[1])

b_i = 0
ans = 0
for aa, num in a_sort:
    while b_i < n and b_sort[b_i][1] < aa:
        b_i += 1
    while b_i < n and b_sort[b_i][1] == aa:
        print(aa, num, b_sort[b_i][0], c.get(b_sort[b_i][0], 0))
        ans += num*c.get(b_sort[b_i][0], 0)
        b_i += 1

print(ans)