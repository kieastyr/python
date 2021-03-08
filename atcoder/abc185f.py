import sys
def input():
    return sys.stdin.readline()[:-1]

num = 5
n, q = map(int, input().split())
a = [[0 for _ in range(2**num)] for _ in range(num+1)]
a[0][:n] = list(map(int, input().split()))
for i in range(num):
    for j in range(2**(num-1-i)):
        a[i+1][j] = a[i][2*j]^a[i][2*j+1]

print(a)

q1 = {}
for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        if q1.get(x):
            q1[x].append(y)
        else:
            q1[x] = [y]
    else:
        ans = 0
        for i in range(x, y+1):
            ans ^= a[i]
            if q1.get(i):
                for ys in q1[i]:
                    ans ^= ys
        print(ans)


