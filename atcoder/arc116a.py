import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
t =  int(input())
for _ in range(t):
    n = int(input())
    if n%2 != 0:
        print("Odd")
    elif n%4 == 0:
        print("Even")
    else:
        print("Same")
