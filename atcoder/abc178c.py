mod = int(1e9+7)
n = int(input())
ans1 = 1
ans2 = 1
ans3 = 1
for i in range(n):
    ans1 *= 10
    ans1 %= mod
    ans2 *= 9
    ans2 %= mod
    ans3 *= 8
    ans3 %= mod

ans = ans1 - 2*ans2 + ans3

print(ans%mod)