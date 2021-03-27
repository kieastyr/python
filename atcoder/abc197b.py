import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

H, W, X, Y = map(int, input().split())
s = []

for _ in range(H):
    s.append(list(input()))

ans = 1
for x in range(X-2, -1, -1):
    if s[x][Y-1] == '.':
        ans += 1
    else:
        break
for x in range(X, H):
    if s[x][Y-1] == '.':
        ans += 1
    else:
        break

for y in range(Y-2, -1, -1):
    if s[X-1][y] == '.':
        ans += 1
    else:
        break
for y in range(Y, W):
    if s[X-1][y] == '.':
        ans += 1
    else:
        break

print(ans)