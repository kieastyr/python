import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

n = int(input())
max_num = 10000

# a = [2*3*5*7, 2*3*5*11, 2*3*7*11, 2*5*7*11, 3*5*7*11]
# p = [2, 3, 5, 7, 11]
# k = [1, 1, 1, 1, 1]
a = set()

num = 6
i = 2
while num*i <= max_num:
    a.add(num*i)
    i += 1

num = 10
i = 2
while num*i <= max_num:
    a.add(num*i)
    i += 1

num = 15
i = 2
while num*i <= max_num:
    a.add(num*i)
    i += 1
print(max(a))
ans = "6 10 15 " + " ".join(map(str, list(a)[:n-3]))
print(ans)  

