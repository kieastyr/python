n, x, y = map(int, input().split())
edge = [[] for _ in range(n+1)]
dist = [[abs(i-j) for i in range(n+1)] for j in range(n+1)]
counter = [0 for i in range(n)]
for i in range(1, n):
    edge[i].append(i+1)
    edge[i+1].append(i)
edge[x].append(y)
edge[y].append(x)
for i in range(y+1):
    for j in range(x, n+1):
        if j > i:
            new_dist = abs(x-i)+abs(y-j)+1
            if new_dist < dist[i][j]:
                dist[i][j] = new_dist

for i in range(1, n+1):
    for num in dist[i][i+1:]:
        counter[num] += 1
# print(dist)

for num in counter[1:]:
    print(num)
