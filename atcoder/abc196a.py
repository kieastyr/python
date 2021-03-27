import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

a, b = map(int, input().split())
c, d = map(int, input().split())
print(b-c)