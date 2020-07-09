import random
# n, m, k = map(int, input().split())
n, m, k = random.randint(1, 10**5), random.randint(1, 10**5), random.randint(10**8, 10**9)
# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))
a_list = [random.randint(1, 10**3) for i in range(n)]
b_list = [random.randint(1, 10**3) for i in range(m)]
# print(n,m,k)
# print(a_list[0], b_list[0])
a_sum = [0]
b_sum = [0]
max_a = 0
for i in range(1, max(n+1, m+1)):
    if i < n+1:
        a_sum.append(a_sum[i-1] + a_list[i-1])
        if a_sum[i] <= k:
            max_a = i
    if i < m+1:
        b_sum.append(b_sum[i-1] + b_list[i-1])

ans = 0
j = m
for i in range(0, max_a+1):
    while b_sum[j] > k - a_sum[i]:
        j -= 1
    ans = max(ans, i+j)
        
print(ans)
# print(n+m) 