n = int(input())
a_array = list(map(int, input().split()))
a_array.insert(0, 0)
x_sum = {}
x_dis = {}

for i in range(1, n+1):
    a_sum = i + a_array[i]
    if a_sum in x_sum:
        x_sum[a_sum].append(i)
    else:
        x_sum[a_sum] = [i]
    if not(a_sum in x_dis):
        x_dis[a_sum] = []

    a_dis = i - a_array[i]
    if a_dis > 0:
        if a_dis in x_dis:
            x_dis[a_dis].append(i)
        else:
            x_dis[a_dis] = [i]
        if not(a_dis in x_sum):
            x_sum[a_dis] = []

# print(x_sum)
# print(x_dis)
count = 0
for k in x_sum.keys():
    count += len(x_sum[k]) * len(x_dis[k])

print(count)
