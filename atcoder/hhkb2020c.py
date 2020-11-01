n = int(input())
num = {i:[i-1, i+1] for i in range(-1, 200002)}
p_list = map(int, input().split())

for p in p_list:
    if num[p][0] != -100:
        num[num[p][0]][1] = num[p][1]
        num[num[p][1]][0] = num[p][0]
        num[p][0] = -100
    print(num[-1][1])