import sys
def input():
    return sys.stdin.readline()[:-1]

a, b, x, y = map(int, input().split())

ans = x
if a < b:
    ans += (b-a)*min(2*x, y)
elif a > b:
    ans += (a-b-1)*min(2*x, y)

print(ans)
