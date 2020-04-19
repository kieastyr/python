'''
Created on 2019/07/08

@author: B4
'''

mod = 1e9+7

def dfs(k, edge, now, pred):
    if pred==0:
        colorNum = k-1
    else:
        colorNum = k-2
    if len(edge[now])>=k:
        return 0
    else:
        count_case = 1
        for e in edge[now]:
            if e!=pred:
                count_case *= colorNum
                colorNum -= 1
                count_case %= mod
        for e in edge[now]:
            if e!=pred:
                count_case *= dfs(k, edge, e, now)
                count_case %= mod
        return count_case

if __name__ == '__main__':
    n, k = map(int, input().split())
    edge = [[] for i in range(n+1)]
    for i in range(n-1):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    answer = int(k*dfs(k,edge,1,0)%mod)
    print(answer)
    