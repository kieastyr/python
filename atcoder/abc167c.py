n, m, x = map(int, input().split())
a = []
max_sum = [0 for _ in range(m)]
price_sum = 0
for i in range(n):
    input_list = list(map(int, input().split()))
    a.append([input_list[0], input_list[1:]])
    price_sum += input_list[0]
    for j in range(m):
        max_sum[j] += input_list[j + 1]

flag = 0
for j in range(m):
    if max_sum[j] < x:
        flag = 1
if flag:
    print(-1)
else:
    min_price = price_sum
    for pattern in range(1, 2 ** n):
        flag = 0
        now_price = price_sum
        now_sum = max_sum.copy()
        # print(bin(pattern))
        for i in range(n):
            if pattern & 1 << i:
                now_price -= a[i][0]
                for j in range(m):
                    now_sum[j] -= a[i][1][j]

        # print(now_price, now_sum)
        for j in range(m):
            if now_sum[j] < x:
                flag = 1
        if not flag and now_price < min_price:
            min_price = now_price

    print(min_price)
