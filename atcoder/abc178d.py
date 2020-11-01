mod = 1000000007
s = int(input())
max_num = s//3
if max_num < 1:
    print(0)
else:
    ans = 1
    for bar_num in range(1, max_num):
        dist_num = s - 3*(bar_num+1)
        prod = 1
        b = bar_num
        for i in range(dist_num+bar_num, dist_num, -1):
            prod *= i
            if b != 1 and prod%b == 0:
                prod //= b
                b -= 1
            elif b == 1:
                prod %= mod
        # print(dist_num, bar_num, prod)
        ans += prod
        # ans %= mod
    print(ans%mod)