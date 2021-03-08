n = int(input())
place = [list(map(int, input().split())) for _ in range(n)]
dp = [[1e20 for _ in range(2**n)] for __ in range(n)]
cost = [[0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            if place[i][2] < place[j][2]:
                num = 3
            else:
                num = 2
            
            for xyz in range(num):
                cost[i][j] += abs(place[i][xyz] - place[j][xyz])


for i in range(n):
    dp[i][2**i] = cost[0][i]

for s in range(1, 2**n):
    reached = []
    for i in range(n):
        if s >> i & 1:
            reached.append(i)

    # print(reached)
    for i in range(1, n):
        dp[i][s] = min([dp[j][s-2**i] + cost[j][i] if i!=j else 1e20 for j in reached])

print(min([dp[i][2**n-1]+cost[i][0] for i in range(1, n)]))
