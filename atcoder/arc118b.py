import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

k, n, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(lambda x: x*m/n, a_list))
b_list_f = list(map(math.floor, b_list))
b_deci = [(i, n*b_list_f[i]-m*a_list[i]) for i in range(k)]
b_deci_sorted = sorted(b_deci, key=lambda x: x[1])
# print(b_deci_sorted)

for i in range(m-sum(b_list_f)):
    j = b_deci_sorted[i][0]
    b_list_f[j] += 1

print(' '.join(map(str, b_list_f)))
