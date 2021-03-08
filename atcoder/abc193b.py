import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a_list = []
p_list = {}
x_list = []

for i in range(n):
    a, p, x = map(int, input().split())
    a_list.append(a)
    p_list[i] = p
    x_list.append(x)

p_sort = sorted(p_list.items(), key=lambda x: x[1])

for i, p in p_sort:
    if x_list[i]-a_list[i] > 0:
        print(p)
        exit()

print(-1)


