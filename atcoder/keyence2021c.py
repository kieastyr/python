import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

h, w, k = map(int, input().split())
all = pow(3, h*w-k, mod)
inv = (3, -2, mod)
dp = [[[all, all] for _ in range(w+1)] for _ in range(h+1)]
l = [["" for _ in range(w+1)] for _ in range(h+1)]

for _ in range(k):
    h1, w1, c1 = input().split()
    h1 = int(h1)
    w1 = int(w1)
    l[h1][w1] = c1

# print(l)

if l[1][1] == "R":
    dp[1][1][0] = 0
elif l[1][1] == "D":
    dp[1][1][1] = 0
elif l[1][1] == "":
    dp[1][1] = [all//3*2, all//3*2]

for w1 in range(2, w+1):
    num = dp[1][w1-1][1]
    dp[1][w1] = [num, num]
    if l[1][w1] == "R":
        dp[1][w1][0] = 0
    elif l[1][w1] == "D":
        dp[1][w1][1] = 0
    elif l[1][w1] == "":
        dp[1][w1] = [num//3*2, num//3*2]
        
for h1 in range(2, h+1):
    num = dp[h1-1][1][0]
    dp[h1][1] = [num, num]
    if l[h1][1] == "R":
        dp[h1][1][0] = num
    elif l[h1][1] == "D":
        dp[h1][1][1] = num
    elif l[h1][1] == "":
        dp[h1][1] = [num//3*2, num//3*2]

# print(dp)

for h1 in range(2, h+1):
    for w1 in range(2, w+1):
        num = dp[h1][w1-1][0] + dp[h1-1][w1][1]
        dp[h1][w1] = [num, num]
        if l[h1][w1] == "R":
            dp[h1][w1][0] = 0
        elif l[h1][w1] == "D":
            dp[h1][w1][1] = 0
        elif l[h1][w1] == "":
            dp[h1][w1] = [num//3*2, num//3*2]
        # print(h1, w1, dp[h1][w1])

print(dp[h][w][0]+dp[h][w][1])

