n, m = map(int, input().split())
edge = [[] for i in range(n+1)]
reached = [0 for _ in range(n+1)]
guide = [0 for i in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

print("Yes")
queue = [(e, 1) for e in edge[1]]
counter = 0
while counter < n-1:
    # print(queue)
    e, now = queue.pop(0)
    if reached[e] == 0:
        counter += 1
        reached[e] = 1
        guide[e] = now
        # edge[e].remove(now)
        for next in edge[e]:
            if next != 1 and reached[next] == 0:
                queue.append((next, e))

for i in range(2, n+1):
    print(guide[i])
