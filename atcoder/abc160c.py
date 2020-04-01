k, n = map(int, input().split())
a = list(map(int, input().split()))
dist = []
for i in range(n-1):
    dist.append(a[i+1]-a[i])
dist.append(k-a[n-1]+a[0])
print(k-max(dist))