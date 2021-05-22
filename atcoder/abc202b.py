import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

s_list = list(input())[::-1]
ans = ""
for s in s_list:
    if s == '6':
        ans += '9'
    elif s == '9':
        ans += '6'
    else:
        ans += s

print(ans)