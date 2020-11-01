mod = pow(10, 9)+7

n = int(input())
a_list = list(map(int, input().split()))
a_sum = sum(a_list)
a_sq = sum(map(pow, a_list, [2]*n))

a = (a_sum**2//2)%mod
b = (a_sq//2%mod)
print((a-b)%mod)