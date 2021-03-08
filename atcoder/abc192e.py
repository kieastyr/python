import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

from heapq import *

def dijkstra(start,node,edge):
    #始点sから各頂点への最短距離
    #node:頂点数
    #d:各頂点へのコスト(存在しないときはinf)
    #q:キュー(スタートからのコスト,頂点)
    d = [float("inf")] * (node+1)
    d[start] = 0
    #スタートをキューに入れる
    q = [(0,start)]

    while(len(q) != 0):
    #キューの先頭を取得
        ci,i = heappop(q)
        if(d[i] < ci):
            continue
    #キューの先頭から繋がっている頂点を探索
        for j, costs in edge[i].items():
            min_cost = float("inf")
            for cost in costs:
                min_cost = min(min_cost, d[i]+cost[0]+(cost[1]-((d[i]-1)%cost[1]+1)))        
            if(d[j] > min_cost):
                d[j] = min_cost
                heappush(q,(d[j], j))
    return d

#入力
n, m ,x, y = map(int, input().split())
edge = {i:{} for i in range(1, n+1)}
for _ in range(m):
    a, b, t, k = map(int, input().split())
    if edge[a].get(b):
        edge[a][b].append([t, k])
        edge[b][a].append([t, k])
    else:
        edge[a][b] = [[t, k]]
        edge[b][a] = [[t, k]]

# print(edge)
ans = dijkstra(x, n, edge)
if ans[y] == float("inf"):
    print(-1)
else:
    print(ans[y])