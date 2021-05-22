import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353

a, b = map(int, input().split())
if a >= b:
    posi = list(range(1000-a+1, 1001))
    nega = [-sum(posi[b-1:])]
    nega.extend(map(lambda x:-x, posi[:b-1]))
else:
    nega = list(range(-1000+b-1, -1001, -1))
    posi = [-sum(nega[a-1:])]
    posi.extend(map(lambda x:-x, nega[:a-1]))

print(" ".join(map(str, posi+nega)))

