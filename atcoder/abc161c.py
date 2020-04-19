n, k = map(int, input().split())
if n < k:
    if k - n < n:
        print(k - n)
    else:
        print(n)
elif n % k > k / 2:
    print(k - n % k)
else:
    print(n % k)
