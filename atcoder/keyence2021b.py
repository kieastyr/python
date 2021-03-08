import sys
import collections
def input():
    return sys.stdin.readline()[:-1]

n, k = map(int, input().split())
a = list(map(int, input().split()))
c = collections.Counter(a)

num = k
ans = 0
for i in range(n):
    if num == 0:
        break
    elif c[i] < num:
        ans += i*(num-c[i])
        num = c[i]

print(ans)
        

