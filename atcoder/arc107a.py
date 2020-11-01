mod = 998244353
a, b, c = map(int, input().split())
print(a*(a+1)*b*(b+1)*c*(c+1)//8%mod)