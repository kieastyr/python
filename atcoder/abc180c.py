n = int(input())
if n == 1:
    print(1)
else:
    ans = [1, n]
    i = 2
    while i*i <= n:
        if n % i == 0:
            if i == n//i:
                ans.append(i)
            else:
                ans.extend([i, n//i])
        i += 1

    ans.sort()
    for a in ans:
        print(a)
