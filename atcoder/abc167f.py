n = int(input())
s_num = [0 for _ in range(n)]
s_num_min = [0 for _ in range(n)]
for i in range(n):
    kakko_in = input()
    for s_in in kakko_in:
        if s_in == '(':
            s_num[i] += 1
        else:
            s_num[i] -= 1
        if s_num[i] < s_num_min[i]:
            s_num_min[i] = s_num[i]

if sum(s_num) != 0:
    print("No")
else:
    now_sum = 0
    now_min_sum = 0
    s_num_index = s_num.argsort()[::-1]
    # print(s_num_index)
    # print(s_num_min_index)
    yet = [1 for _ in range(n)]
    i = 0
    flag = 0
    while i < n:
        index = s_num_index[i]
        if now_sum + s_num_min[index] >= 0:
            flag = 0
            now_sum += s_num[index]
            i += 1
        else:
            flag = 1
            break
        # elif i < n-1:
        #     if flag:
        #         break
        #     temp = s_num_index[i+1]
        #     s_num_index[i] = temp
        #     s_num_index[i+1] = index
        #     flag = 1
    if flag:
        print("No")
    else:
        print("Yes")
