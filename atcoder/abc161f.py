n = int(input())
k = 2
count = set()
while k * k <= n:
    if n % k == 1:
        count.add(k)
        count.add((n-1)//k)
    elif n % k == 0:
        n_copy = n
        while n_copy % k == 0:
            n_copy //= k
        if n_copy % k == 1:
            count.add(k)
    k += 1
if n > 2:
    count.add(n-1)
count.add(n)
print(len(count))
