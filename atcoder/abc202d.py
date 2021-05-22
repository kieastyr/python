import sys
import math
from collections import Counter

def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

def narabi(a, b):
    num = 1
    aa = 2
    bb = 2
    for i in range(2, a+b+1):
        num *= i
        if aa <= a and num%aa == 0:
            num //= aa
            aa += 1
        if bb <= b and num%bb == 0:
            num //= bb
            bb += 1
    return num

a, b, k = map(int, input().split())
all = narabi(a, b)
ans = ''
s_len = a+b
for i in range(s_len):
    thr = a*all//(a+b)
    if k <= thr:
        ans += 'a'
        all = thr
        a -= 1
    else:
        ans += 'b'
        all -= thr
        k -= thr
        b -= 1

print(ans)