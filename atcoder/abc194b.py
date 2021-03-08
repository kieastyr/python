import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())

a, b = {}, {}
for i in range(n):
    aa, bb = map(int, input().split())
    a[i] = aa
    b[i] = bb

a_s = sorted(a.items(), key=lambda x: x[1])
b_s = sorted(b.items(), key=lambda x: x[1])
print(a_s)
print(b_s)

if a_s[0][0] != b_s[0][0]:
    print(max(a_s[0][1], b_s[0][1]))
else:
    print(min(a_s[0][1]+b_s[0][1], max(a_s[1][1], b_s[0][1]), max(a_s[0][1], b_s[1][1])))
