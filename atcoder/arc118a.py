import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

t, n = map(int, input().split())
print((100*n-1)//t+n)
