n, k = map(int, input().split())
ans = 0
if k < 0:
    k = -k
cd = 2
while cd + k <= 2*n:
    if cd <= n:
        term1 = cd-1
    else:
        term1 = 2*n-cd+1
    if cd + k - 1 <= n:
        term2 = cd+k-1
    else:
        term2 = (2*n-(cd+k)+1)
    ans += term1*term2
    cd += 1


print(ans)