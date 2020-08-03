n = int(input())
s = input()
start = 0
end = n-1
count = [[0, 0] for _ in range(n)]
start_w = 0
end_r = 0
for i in range(n):
    count[i][0] = start_w
    if s[i] == "W":
        start_w += 1
for i in reversed(range(n)):
    count[i][1] = end_r
    if s[i] == "R":
        end_r += 1

print(min(map(max,count)))