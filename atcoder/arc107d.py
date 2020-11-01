mod = 998244353
n, k = map(int, input().split())
dp = [[0 for j in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    dp[i][1] = 1

for i in range(1, n+1):
    for j in reversed(range(2, i+1)):
        if 2*j > i:
                dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i][2*j])%mod

# for i in dp:
#     print(i)
print(dp[n][k])
