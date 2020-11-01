import random
import math
n, s = input().split()
n = int(n)
# n = 5000
# s = [random.choice(['A', 'T', 'G', 'C']) for i in range(n)]
need_num = {'AT': 0, 'GC': 0}
dna_sum = [need_num.copy()]

ans = 0

for s_i in s:
    if s_i == 'A':
        need_num['AT'] += 1
    elif s_i == 'T':
        need_num['AT'] -= 1
    elif s_i == 'G':
        need_num['GC'] += 1
    elif s_i == 'C':
        need_num['GC'] -= 1
    dna_sum.append(need_num.copy())

for end in range(2, n+1):
    start = 0
    while start < end:
        dis = []
        for k in ['AT', 'GC']:
            dis.append(dna_sum[end][k] - dna_sum[start][k])
        if dis[0] == 0 and dis[1] == 0:
            ans += 1
            start += 2
        else:
            start += abs(dis[0]) + abs(dis[1])

print(ans)
