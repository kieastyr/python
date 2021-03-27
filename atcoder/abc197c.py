import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a_list = list(map(int, input().split()))

ans = float("inf")
for sikiri in range(2**(n-1)):
    group = []
    g_num = 0
    group.append(a_list[0])
    for i in range(n-1):
        if sikiri>>i & 1 == 0:
            group[g_num] |= a_list[i+1]
        else:
            g_num += 1
            group.append(a_list[i+1])
    ans1 = 0
    for g in group:
        ans1 ^= g
    # print(sikiri, group, ans1)
    ans = min(ans, ans1)

print(ans)





