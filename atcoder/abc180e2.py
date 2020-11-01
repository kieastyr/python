n = int(input())
place = [list(map(int, input().split())) for _ in range(n)]
cost = [{} for _ in range(n)]

def dist(a, b):
    d = 0
    for k in range(2):
        d += abs(place[b][k] - place[a][k])
    if place[b][2] - place[a][2] > 0:
        d += place[b][2] - place[a][2]
    return d


def bitdp(now, reached):
    if reached == 1:
        if cost[now].get(reached) is None:
            cost[now][reached] = dist(0, now)
        return cost[now][reached]
    else:
        min_cost = float('inf')
        for i in range(1, n):
            if (reached >> i) & 1 == 1:
                if cost[i].get(reached-2**i) is None:
                    cost[now][reached] = dist(i, now) + bitdp(i, reached-2**i)
                else:
                    cost[now][reached] = dist(i, now) + cost[i][reached-2**i]
                # print(d)
                min_cost = min(min_cost, cost[now][reached])
        return min_cost

ans = [bitdp(i, 2**n-2**i-1)+dist(i, 0) for i in range(1, n)]
print(min(ans))
