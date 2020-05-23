n, k = map(int, input().split())
okasi = [0]*(n+1)
for _ in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in range(d):
        okasi[a[i]] += 1

count = 0
for i in range(1, n+1):
    if okasi[i] == 0:
        count += 1

print(count)
