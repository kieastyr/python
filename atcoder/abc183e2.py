

import sys
def input():
    return sys.stdin.readline()

mod = int(1e9+7)

# h, w = 1000, 1000
# s = [["." for _ in range(w)] for _ in range(h)]

# import time
# t1 = time.time()

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dir = [[[0 for k in range(4)] for j in range(w)] for i in range(h)]
dir[0][0][3] = 1

d = [(-1, -1), (-1, 0), (0, -1)]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            k = 0
            for ii, jj in d:
                if i+ii >= 0 and j+jj >= 0 and s[i+ii][j+jj] == ".":
                    dir[i][j][3] += dir[i+ii][j+jj][3]+dir[i+ii][j+jj][k]
                    dir[i][j][k] = dir[i+ii][j+jj][3]+dir[i+ii][j+jj][k] % mod
                k += 1
            dir[i][j][3] %= mod
# print("\n".join(map(str, reached)))
print(dir[h-1][w-1][3])
# print(time.time()-t1)