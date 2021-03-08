n, k = map(int, input().split())
t = [list(map(int, input().split())) for _ in range(n)]
# print(t)

def nap(now, rem, time):
    if len(rem) == 0:
        if time+t[now][0] == k:
            return 1
        else:
            return 0
    ans = 0
    for i in rem:
        ans += nap(i, rem-{i}, time+t[now][i])
    return ans

print(nap(0, set(range(1, n)), 0))

