import sys
def input():
    return sys.stdin.readline()[:-1]

h, w, m = map(int, input().split())

x_max = {i: h for i in range(1, w+1)}
y_max = {i: w for i in range(1, h+1)}
for i in range(m):
    x, y = map(int, input().split())
    x_max[y] = min(x_max[y], x)
    y_max[x] = min(y_max[x], y)

x_sum = sum([x_max[k] for k in range(1, y_max[1])])
y_sum = sum([y_max[k] for k in range(1, x_max[1])])

print(x_sum, y_sum)