import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
c_set = {}
c_maxmin = {0: [0, 0]}
c_cost = {}
color = []

for _ in range(n):
    x, c = map(int, input().split())
    if c_set.get(c):
        c_set[c].append(x)
        c_maxmin[c][0] = min(c_maxmin[c][0], x)
        c_maxmin[c][1] = max(c_maxmin[c][1], x)
    else:
        color.append(c)
        c_set[c] = [x]
        c_maxmin[c] = [x, x]

color.sort()
ans = 0
for c in color:
    c_cost[c] = c_maxmin[c][1] - c_maxmin[c][0]
    ans += c_cost[c]

print(c_cost)

ans1 = ans+c_maxmin[color[0]][0]
sippo = 1
for i in range(len(color)-1):
    c1x = c_maxmin[color[i]][sippo]
    c2 = color[i+1]
    if i+2 < len(color):
        c3 = color[i+2]
    else:
        c3 = 0
    if c_maxmin[c2][0] == c_maxmin[c2][1]:
        ans1 += abs(c1x-c_maxmin[c2][0])
        sippo = 1
    else:
        cost1 = min(abs(c1x-c_maxmin[c2][0])+abs(c_maxmin[c3][0]-c_maxmin[c2][1]), 
                    abs(c1x-c_maxmin[c2][0])+abs(c_maxmin[c3][1]-c_maxmin[c2][1]))
        cost2 = min(abs(c1x-c_maxmin[c2][1])+abs(c_maxmin[c3][0]-c_maxmin[c2][0]), 
                    abs(c1x-c_maxmin[c2][1])+abs(c_maxmin[c3][1]-c_maxmin[c2][0]))
        if cost1 > cost2:
            ans1 += abs(c1x-c_maxmin[c2][0])
            sippo = 1
            print(color[i], c2, abs(c1x-c_maxmin[c2][0]))
        else:
            ans1 += abs(c1x-c_maxmin[c2][1])
            sippo = 0
            print(color[i], c2, abs(c1x-c_maxmin[c2][1]))

ans1 += c_maxmin[color[-1]][sippo]
print(ans1)

    
        


