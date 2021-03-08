import sys
def input():
    return sys.stdin.readline()[:-1]

n, q = map(int, input().split())
a = list(map(int, input().split()))
a_xor = [a[0]]
for i in range(n):
    a_xor.append(a_xor[-1]^a[i])

# print(a)

q1 = {}

for _ in range(q):
    t, x, y = map(int, input().split())
    if t == 1:
        a_xor = 
        if q1.get(x):
            q1[x] ^= y
        else:
            q1[x] = y
    else:
        ans = a_xor[y]^a_xor[x-1]
        for key in q1.keys():
            if x-1 <= key <= y:
                ans ^= q1[key]
        print(ans)


