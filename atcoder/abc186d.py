import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)

ans = 0
j = n-1
for ai in a:
    ans += j*ai
    j -= 2

print(ans)