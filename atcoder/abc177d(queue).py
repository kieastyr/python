import random
import sys

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
ans = list(g_mem.values())
for now in range(1, g_num+1):
    if g_reached[now] == 0:
        g_reached[now] = 1
        if edge.get(now):
            count = g_mem[now]
            queue = set(edge[now])
            while len(queue) > 0:
                next_now = queue.pop()
                if g_reached[next_now] == 0:
                    g_reached[next_now] = 1
                    count += g_mem[next_now]
                    queue |= edge[next_now]
                queue -= {now}
                now = next_now
            ans.append(count)


# print(ans)
if len(ans) > 0:
    print(max(ans))
else:
    print(1)
