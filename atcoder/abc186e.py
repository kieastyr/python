import sys
def input():
    return sys.stdin.readline()[:-1]

def extGCD(a, b, x, y):
    if b == 0:
        return a, 1, 0
    else:
        d, y, x = extGCD(b, a%b, y, x)
        y += a//b * x
        return d, x, y

t = int(input())
for _ in range(t):
    n, s, k = map(int, input().split())
    if k > n:
        k %= n
    d, x, y = extGCD(n, k, 1, 0)
    # print(d, x, y)
    if s%d != 0:
        print(-1)
    else:
        if n*x - k*y > 0:
            a = x*s//d
            b = y*s//d
            c = min(a//k, b//n)
            print(b-n*c)
        else:
            a = x*s//d
            b = y*s//d
            c = max((a-1)//k+1, (b-1)//n+1)
            print(-b+n*c)
            