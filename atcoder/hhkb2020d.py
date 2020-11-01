mod = 1000000007
n, a, b = map(int, input().split())

if n - 2*b >= a:
    a_put_1d = (n-2*b-a+1)%mod
    b_put = ((n-b+1)%mod)**2 %mod
    a_kabu = (a+2*b-1)%mod
    b_kabu = ((b**2 + b)//2%mod - a+1) %mod
    ans1 = a_put_1d**2 * b_put %mod - (((a_kabu **2)%mod)*(a_put_1d**2)) %mod
    ans2 = a_put_1d*b%mod * b_put %mod - ((a_kabu * b_kabu %mod)*(a_put_1d*b %mod) %mod)
    ans3 = b **2 %mod * b_put %mod - ((b_kabu **2%mod)*(b**2)) %mod

    print(ans1)
    print(ans2)
    print(ans3)
    print((ans1+ans2*4+ans3*4)%mod)

elif n >= 2*b:
    a_put_1d = (n-2*b-a+1)%mod
    b_put = ((n-b+1)%mod)**2 %mod
    a_kabu = (a+2*b-1)%mod
    b_kabu = ((b**2 - b)//2%mod + a+1) %mod
    ans2 = a_put_1d*(n//2-b+1)%mod * b_put %mod - ((a_kabu * b_kabu %mod)*(a_put_1d*b %mod) %mod)
    ans3 = (n//2-b+1) **2 %mod * b_put %mod - ((b_kabu **2%mod)*(b**2)) %mod
    print(ans2)
    print(ans3)
    print((ans2*4+ans3*4)%mod)
    