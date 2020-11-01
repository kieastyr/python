import sys
sys.setrecursionlimit(5000)

mod = 998244353
n, k = map(int, input().split())
ans = {1: 1}
seg = [tuple(map(int, input().split())) for _ in range(k)]
seg.sort(key=lambda x: x[0])

def dp(i):
    if ans.get(i) is None:
        ans[i] = 0
    for l, r in seg:
        if l >= i:
            break
        else:
            s = sum((ans[i-j] if ans.get(i-j) else dp(i-j)) for j in range(l, min(i, r+1)))
            ans[i] += s
            ans[i] %= mod
    return ans[i]

print(dp(n))

