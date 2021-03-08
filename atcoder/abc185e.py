import sys
def input():
    return sys.stdin.readline()[:-1]

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b = []

a.insert(0, 0)
a.append(n+1)

for i in range(m+1):
    if a[i+1]-a[i] > 1:
        b.append(a[i+1]-a[i]-1)

if len(b) == 0:
    print(0)
else:
    k = min(b)
    # print(k)
    ans = 0
    for bi in b:
        ans += (bi-1)//k + 1

    print(ans)