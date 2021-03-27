import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

H, W, A, B = map(int, input().split())
dp1 = [[[[0 for _ in range(2)] for _ in range(A)]for _ in range(W-1)] for _ in range(H)]
dp2 = [[[[0 for _ in range(2)] for _ in range(A)]for _ in range(W)] for _ in range(H-1)]
dp1[0][0][0][0] = 1
dp1[0][0][1][1] = 1
dp2[0][0][0][0] = 1
dp2[0][0][1][1] = 1

for a in range(A):
    for w in range(1, W-1):
        dp1[0][w][a][0] = dp1[0][w-1][a][1]*dp1[0][w-1][a][0]
        dp1[0][w][a][1] = dp1[0][w-1][a-1][0]
    
    for h in range(1, H-1):
        dp1[h][0][a][0] = dp1[h][0][a][1]*dp1[h][0][a][0]
        dp1[h][0][a][1] = dp1[h][0][a-1][0]