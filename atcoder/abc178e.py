import numpy as np

def dist(d1, d2):
    return abs(d1[0]-d2[0]) + abs(d1[1]-d2[1])

n = int(input())
list1 = np.zeros((n))
list2 = np.zeros((n))
xy_list = []
for i in range(n):
    x, y = map(int, input().split())
    xy_list.append([x, y])
    list1[i] = x+y
    list2[i] = x-y

num = np.zeros((4), dtype=int)
num[0] = np.argmax(list1)
num[1] = np.argmax(list2)
num[2] = np.argmin(list1)
num[3] = np.argmin(list2)

ans = 0
for d1 in range(4):
    for d2 in range(d1+1, 4):
        # print(num[d1], num[d2], dist(xy_list[num[d1]], xy_list[num[d2]]))
        ans = max(ans, dist(xy_list[num[d1]], xy_list[num[d2]]))

print(ans)