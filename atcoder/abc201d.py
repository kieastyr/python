import sys
import math

def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

H, W = map(int, input().split())

if (H+W)%2 == 0:
    goal = 'Aoki'
    notgoal = 'Takahashi'
else:
    notgoal = 'Aoki'
    goal = 'Takahashi'

dp = [list(map(lambda x: int(x+'1'), list(input()))) for _ in range(H)]
# print(dp)
dp[0][0] = 0

if H >= 2 and W >= 2:
    dp[1][1] += dp[0][0]-min(dp[1][0], dp[0][1])
for w in range(2, W):
    dp[0][w] += dp[0][w-2]-dp[0][w-1]
    if H >= 2:
        dp[1][w] += max(dp[1][w-2]-dp[1][w-1], dp[0][w-1]-min(dp[0][w], dp[1][w-1]))

for h in range(2, H):
    dp[h][0] += dp[h-2][0]-dp[h-1][0]
    if W >= 2:
        dp[h][1] += max(dp[h-2][1]-dp[h-1][1], dp[h-1][0]-min(dp[h][0], dp[h-1][1]))

for h in range(2, H):
    for w in range(2, W):
        dp[h][w] += max(
            dp[h-2][w]-dp[h-1][w], 
            dp[h-1][w-1]-min(dp[h][w-1], dp[h-1][w]), 
            dp[h][w-2]-dp[h][w-1])
# print(dp)

if H==1 and W==1:
    notgoaldp = dp[H-1][W-1]
elif H==1:
    notgoaldp = dp[H-1][W-2]
elif W==1:
    notgoaldp = dp[H-2][W-1]
else:
    notgoaldp = max(dp[H-2][W-1], dp[H-1][W-2])

if dp[H-1][W-1] > notgoaldp:
    print(goal)    
elif dp[H-1][W-1] == notgoaldp:
    print('Draw')
else:
    print(notgoal)