import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, m = map(int, input().split())
a = list(map(int, input().split()))
num_set = set(i for i in range(n+1))
num_dict = {i: 0 for i in range(n)}
for i in range(m):
    num_set -= {a[i]}
    num_dict[a[i]] = i
# print(num_set)
ans = min(num_set)
for i in range(m, n):
    if i - num_dict[a[i]] > m:
        ans = min(a[i], ans)
    num_dict[a[i]] = i
    # print(num_dict, i-m)
    if num_dict[a[i-m]] == i-m:
        ans = min(a[i-m], ans)


print(ans)
