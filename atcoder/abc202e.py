import sys
import math
from collections import Counter

def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
p_dict = {i: v for i, v in zip(range(2, n+1), map(int, input().split()))}
q = int(input())

tree = {i: [] for i in range(1, n+1)}
for i, v in p_dict.items():
    tree[v].append(i)

# print(tree)
queue = {1}
data = {1: [0, [1]]}
depth = {0: {1: [1]}}
while len(queue) > 0:
    i = queue.pop()
    for j in tree[i]:
        queue.add(j)
        dep = data[i][0]+1
        data[j] = []
        data[j].append(dep)
        data[j].append(data[i][1]+[j])
        if depth.get(dep) is None:
            depth[dep] = {}
        for k in data[j][1]:
            if depth[dep].get(k):
                depth[dep][k] += 1
            else:
                depth[dep][k] = 1

print(data)
print(depth)

for _ in range(q):
    u, d = map(int, input().split())
    ans = 0
    if depth.get(d) and depth[d].get(u):
        print(depth[d][u])
    else:
        print(0)
