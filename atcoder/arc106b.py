# import random
# import time
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# n, m = 200000, 200000
# a = [random.randint(-1000000000, 1000000000) for _ in range(n)]
# b = a
# xy = random.sample(range(20000000), m)
# t1 = time.time()
edge = {i+1:[] for i in range(n)}
for i in range(m):
    x, y = map(int, input().split())
    # x = xy[i]%n + 1
    # y = xy[i]//n + 1
    # if x == y:
    #     y += 1
    edge[x].append(y)
    edge[y].append(x)

# print(edge)

group = [0]*(n+1)
g_num = 1
start = 1
ans = 1
while True:
    a_sum = 0
    b_sum = 0
    while start <= n and group[start] != 0:
        start += 1
    if start > n:
        break
    queue = {start}
    while len(queue) > 0:
        now = queue.pop()
        group[now] = g_num
        a_sum += a[now-1]
        b_sum += b[now-1]
        for next in edge[now]:
            if group[next] == 0:
                queue.add(next)
    if a_sum != b_sum:
        ans = 0
        break
    g_num += 1

if ans == 1:
    print("Yes")
else:
    print("No")

# print(time.time()-t1)
