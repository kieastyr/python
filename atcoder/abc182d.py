n = int(input())
a = list(map(int, input().split()))
a_sum = [a[0]]
a_sum_max_i = [0]
a_sum_sum = [a[0]]
ans = max(0, a[0])

for i in range(1, n):
    next_sum = a_sum[-1]+a[i]
    if a_sum[a_sum_max_i[-1]] < next_sum:
        a_sum_max_i.append(i)
    else:
        a_sum_max_i.append(a_sum_max_i[-1])
    a_sum.append(next_sum)
    ans = max(ans, a_sum_sum[-1]+a_sum[a_sum_max_i[-1]])
    a_sum_sum.append(a_sum_sum[-1]+next_sum)

# print(a_sum_max_i)
# print(a_sum)
# print(a_sum_sum)

print(ans)
