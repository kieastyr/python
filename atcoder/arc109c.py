import sys
def input():
    return sys.stdin.readline()[:-1]


rps_dict = {"R": 11, "P": 7, "S": 5}
rps_invdict = {11: "R", 7: "P", 5: "S"}


def rps(a, b):
    if a == b:
        return a
    else:
        num = 15-(rps_dict[a]+rps_dict[b])%7*2
        return rps_invdict[num]

# a = input()
# b = input()
# print(rps(a, b))

n, k = map(int, input().split())
s = list(input())

dp = [["" for _ in range(2*n)] for _ in range(k+1)]
dp[0][:n] = s.copy()
dp[0][n:2*n] = s.copy()
for i in range(k):
    j = 0
    # print(dp[i])
    while j < n:
        dp[i+1][j] = rps(dp[i][2*j], dp[i][2*j+1])
        j += 1
    dp[i+1][j:2*j] = dp[i+1][:j].copy()

print(dp[k][0])
