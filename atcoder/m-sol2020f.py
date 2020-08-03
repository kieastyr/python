n = int(input())
a_list = []
min_crash = 2e5
for _ in range(n):
    x, y, u = list(input().split())
    x = int(x)
    y = int(y)
    a_list.append([x, y, u])

min_crash = 2e5
x_sort = sorted(a_list, key=lambda a: a[0])
y_sort = sorted(a_list, key=lambda a: a[1])
for i in range(n):
    if i < n-1 and x_sort[i][2] == "R":
        flag = 1
        for x, y, u in x_sort[i+1:]:
            if (y < x_sort[i][1] and u == "U") or (y > x_sort[i][1] and u == "D"):
                if abs(x_sort[i][0]-x) == abs(x_sort[i][1] - y):
                    crash = x - x_sort[i][0]
                    min_crash = min(min_crash, crash)
            elif flag and y == x_sort[i][1] and u == "L":
                flag = 0
                crash = (x - x_sort[i][0])/2
                min_crash = min(min_crash, crash)

    elif i != 0 and x_sort[i][2] == "L":
        for x, y, u in x_sort[:i]:
            if (y < x_sort[i][1] and u == "U") or (y > x_sort[i][1] and u == "D"):
                if abs(x_sort[i][0]-x) == abs(x_sort[i][1] - y):
                    crash = x_sort[i][0]-x
                    min_crash = min(min_crash, crash)
    
    if i < n-1 and y_sort[i][2] == "U":
        for x, y, u in y_sort[i+1:]:
            if x == y_sort[i][0] and u == "D":
                crash = (y - y_sort[i][1])/2
                min_crash = min(min_crash, crash)
                break


if min_crash == 2e5:
    print("SAFE")
else:
    print(int(min_crash*10))
