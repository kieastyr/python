import math
n = int(input())
y_set = set()
xy = [[-100, 100] for y in range(201)]
for _ in range(n):
    x, y = list(map(int, input().split()))
    xy[y+100].append(x)
    y_set.add(y)

y_list = sorted(list(y_set))

for y in range(201):
    if len(xy[y]) > 0:
        xy[y].sort()

dp = [[] for i in range(201)]
r = 100
pred_y = y_list[0]
dp[pred_y+100].extend([xy[pred_y][i+1]-xy[pred_y][i] for i in range(len(xy[pred_y])-1)])
for yi, y in enumerate(y_list[1:]):
    dp[y+100].extend([xy[y][i+1]-xy[y][i] for i in range(len(xy[y])-1)])
    for i, min_r in enumerate(dp[y+100]):
        while yi >= 0 and y-y_list[yi] < min_r:
            

