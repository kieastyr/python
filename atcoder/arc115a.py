import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, m = map(int, input().split())
even = 0
odd = 0
for _ in range(n):
    si = sum(list(map(int, list(input()))))
    if si%2==0:
        even += 1
    else:
        odd += 1

print(even*odd)



