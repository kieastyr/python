import time
import random
n = int(input())
place = [list(map(int, input().split())) for _ in range(n)]
t1 = time.time()

def culc_dist(a, b):
    dist = 0
    for k in range(2):
        d = abs(place[b][k] - place[a][k])
        dist += d
    if place[b][2] - place[a][2] > 0:
        dist += place[b][2] - place[a][2]
    return dist

ans = None
for i in range(100):
    route = random.sample(range(n), n)
    cost = [[i, culc_dist(i, i+1)] for i in range(n-1)]
    cost.append([route[-1], culc_dist(route[-1], 0)])
    s = sum([i[1] for i in cost])
    if ans is None or ans > s:
        ans = s
# print(ans)
# t = 0
# while t < 10:
#     t += 1

while time.time() - t1 < 1.9:
    # print(route)
    r1, r2 = random.sample(range(1, n), 2)
    # print(r1, r2)
    a = route[r1]
    b = route[r2]
    if route[r1-1] == b:
        new1 = culc_dist(a, b)
    else:
        new1 = culc_dist(route[r1-1], b)
    if route[r2-1] == a:
        new2 = culc_dist(b, a)
    else:
        new2 = culc_dist(route[r2-1], a)
    
    cost[r1] = [b, new1]
    cost[r2] = [a, new2]
    route[r1] = b
    route[r2] = a

    now_cost = sum([i[1] for i in cost])
    # print(route, cost, now_cost)
    ans = min(ans, now_cost)

ans = 0
for i in cost:
    ans += i[1]

print(ans)
