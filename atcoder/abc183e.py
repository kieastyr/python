import sys
def input():
    return sys.stdin.readline()[:-1]

mod = int(1e9+7)

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
reached = [[0 for _ in range(w)] for _ in range(h)]
reached[0][0] = 1

d = [[-1, -1], [-1, 0], [0, -1]]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            for dd in d:
                ii, jj = dd
                n = 1
                while i+ii*n >= 0 and j+jj*n >= 0 and s[i+ii*n][j+jj*n] == ".":
                    reached[i][j] += reached[i+ii*n][j+jj*n]
                    reached[i][j] %= mod
                    n += 1

# print("\n".join(map(str, reached)))
print(reached[h-1][w-1])
