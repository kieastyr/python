import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
color = [0 for _ in range(400001)]
group = {}
minus = {i: 0 for i in range(1, 400001)}
combi = {}
for i in range(n):
    a, b = ab[i]
    if color[a] == 0:
        color[a] = 1
    if color[b] == 0:
        color[b] = 1
    if combi.get(a):
        combi[a].add(b)
    else:
        combi[a] = {b}
    if combi.get(b):
        combi[b].add(a)
    else:
        combi[b] = {a}


minus = 0
g_num = 0
queue = set()
for a in combi.keys():
    group[g_num] = set()
    if color[a] == 1:
        color[a] = 2
        group[g_num].add(a)
        queue |= combi[a]
        while len(queue) > 0:
            aa = queue.pop()
            if color[aa] == 1:
                color[aa] = 2
                group[g_num].add(aa)
                queue |= combi[aa]
        g_num += 1

# print(combi)
ans = 0
for g in group.values():
    # print(g)
    node_sum = 0
    for aa in g:
        node_sum += len(combi[aa])
        if aa in combi[aa]:
            node_sum += 1
    ans += node_sum//2 if node_sum//2<len(g) else len(g)
    # print(node_sum)

print(ans)
