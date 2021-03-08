import sys
def input():
    return sys.stdin.readline()[:-1]

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
edge = {i: set() for i in range(1, n+1)}
group_num = {i: 0 for i in range(1, n+1)}

for _ in range(m):
    x, y = map(int, input().split())
    edge[x].add(y)

town = 1
group = {}
queue = edge
g_num = 1
queue = set()
for k in edge.keys():
    group[g_num] = set()
    if group_num[k] == 0:
        group[g_num].add(k)
        queue |= edge[k]
        while len(queue) > 0:
            kk = queue.pop()
            if group_num[kk] == 0:
                group[g_num].add(kk)
                queue |= edge[kk]
        g_num += 1

def dps(t, min_a, max_a):
    if len(edge[t]) == 0:
        if a[t] - min_a > 
        return -10**9
    else:
        max_val = -10**9
        for next_t in edge[t]:
            if max_a < a[next_t]:
                max_a = a[next_t]
            val = max_a - min_a
            if min_a > a[next_t]:
                min_a = a[next_t]
            max_val =  max(max_val, val, dps(next_t, min_a, max_a))
            print(t, next_t, max_a, min_a)

        return max_val


ans = -10**9
for t_set in group.values():
    if len(t_set) > 1:
        t0 = min(list(t_set))
        for t in edge[t0]:
            min_a = min(a[t], a[t0])
            max_a = max(a[t], a[t0])
            val = a[t] - a[t0]
            ans = max(val, dps(t, min_a, max_a), ans)
          
print(ans)