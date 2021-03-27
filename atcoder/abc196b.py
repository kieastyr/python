import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

x = input()
ans = ""
for x_i in x:
    if x_i != ".":
        ans += x_i
    else:
        break

print(ans)
