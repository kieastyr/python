n = int(input())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    a -= 1
    ans += (b**2 + b - a**2 - a) // 2

print(ans)