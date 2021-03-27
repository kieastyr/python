import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
s = input()
print(s[1:]+s[0])