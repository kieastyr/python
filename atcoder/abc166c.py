n, m = map(int, input().split())
h = list(map(int, input().split()))
h.insert(0, -1)
group = {i: 0 for i in range(1, n+1)}
searched = {i: 0 for i in range(1, n+1)}
edge = {i: [] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

count = 0
for i in range(1, n+1):
    flag = 1
    for b in edge[i]:
        if h[i] <= h[b]:
            flag = 0
    if flag:
        count += 1

print(count)
