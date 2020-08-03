def func(a, b, c):
    return a**2 + b**2 + c**2 + a*b + b*c + c*a

n = int(input())
ans = [0]*(n+1)
x, y, z = (1, 1, 1)
flag = 0
while flag == 0:
    if func(x, 1, 1) <= n:
        for y in range(1, x+1):
            for z in range(1, y+1):
                num = func(x, y, z)
                if num <= n and x == y == z:
                    ans[num] += 1
                elif num <= n and (x == y or y == z or z == x):
                    ans[num] += 3
                elif num <= n:
                    ans[num] += 6
    else:
        flag = 1
    x += 1

for i in range(1, n+1):
    print(ans[i])
