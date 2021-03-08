import sys
def input():
    return sys.stdin.readline()[:-1]

mod = int(1e9+7)

a, b = map(int, input().split())
c, d = map(int, input().split())
print(a*d-b*c)

