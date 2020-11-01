import random
import sys
    
sys.setrecursionlimit(100000)
    
n, m = map(int, input().split())
# n, m = 200000, 200000
group = {i: 0 for i in range(1, n+1)}
edge = {}
g_mem = {}
g_num = 0
g_con = set()
    
for i in range(m):
    a, b = map(int, input().split())
    # a, b = random.sample(range(1,n+1), 2)
    if group[a]==0 and group[b] == 0:
        g_num += 1
        group[a] = g_num
        group[b] = g_num
        g_mem[g_num] = 2
    elif group[a] == 0:
        group[a] = group[b]
        g_mem[group[b]] += 1
    elif group[b] == 0:
        group[b] = group[a]
        g_mem[group[a]] += 1
    elif group[a] != group[b]:
        if edge.get(group[a]):
            edge[group[a]].add(group[b])
        else:
            edge[group[a]] = {group[b]}
        if edge.get(group[b]):
            edge[group[b]].add(group[a])
        else:
            edge[group[b]] = {group[a]}
    
# print(g_mem)
# print(sum(g_mem.values()))
# print(edge)
    
g_reached = {i: 0 for i in range(1, g_num+1)}
    
def dps(g_mem, edge, now):
    count = g_mem[now]
    if edge.get(now):
        for e in edge[now]:
            if g_reached[e] == 0:
                g_reached[e] = 1
                count += dps(g_mem, edge, e)
    return count
    
    
ans = []
for now in range(1, g_num+1):
    if g_reached[now] == 0:
        g_reached[now] = 1
        ans.append(dps(g_mem, edge, now))
    
# print(ans)
if len(ans) > 0:
    print(max(ans))
else:
    print(1)