import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a = list(map(int, input().split()))
a2 = [i*i for i in a]
sum_a = sum(a)
sum_a2 = sum(a2)

print(n*sum_a2-sum_a*sum_a)
