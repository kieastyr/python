# import random
# import time
mod = 998244353
n, k = map(int, input().split())
# n, k = 2*10**5, 300
# a = [random.randint(1, int(1e8)) for _ in range(n)]
# t1 = time.time()
a = list(map(int, input().split()))
a_pow = [[1 for _ in range(n)] for _ in range(k+1)]
a_pow[1][:] = a
x_fact = [1 for _ in range(k+1)]
x_factinv = [1 for _ in range(k+1)]
sum_apxf = [0 for _ in range(k+1)]
sum_apxf[0] = n
sum_apxf[1] = sum(a)
sum_apap = [0 for _ in range(k+1)]
sum_apap[0] = n
sum_apap[1] = 2*sum(a)

for i in range(2, k+1):
    # a_pow[i][:] = list(map(lambda x, y: x*y%mod, a_pow[i], a))
    a_pow[i] = [a_pow[i-1][j]*a[j]%mod for j in range(n)]
    x_fact[i] = x_fact[i-1] * i % mod
    x_factinv[i] = x_factinv[i-1] * pow(i, mod-2, mod) % mod
    sum_apxf[i] = sum(a_pow[i]) * x_factinv[i] % mod
    sum_apap[i] = pow(2, i, mod) * sum(a_pow[i]) % mod

# print(a_pow)s
# print(x_fact)
# print(sum_apxf)
# print(sum_apap)

for x in range(1, k+1):
    ans = 0
    for i in range(x+1):
        ans += sum_apxf[i]*sum_apxf[x-i]
        ans %= mod
    ans *= x_fact[x]
    ans %= mod
    ans -= sum_apap[x]
    ans %= mod
    ans *= pow(2, mod-2, mod)

    print(ans % mod)

# print(time.time() - t1)