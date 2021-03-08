import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

x = int(input())
m = int(input())
str_x = list(str(x))
str_m = list(str(m))
ans1 = int(max(str_x))+1
n_min = ans1
n_max = m

while n_max > n_min+1:
    n = (n_max + n_min)//2
    if (len(str_x))*math.log10(n) < (len(str_m)-1)*int(str_m[0]):
        n_min = n
    else:
        n_max = n
    print(n_max, n_min)

n_max += 1
print(n_max, ans1)

while True:
    xn = 0
    for i, xx in enumerate(reversed(str_x)):
        xn += int(xx)*(n_max**i)
    if xn > m:
        print(n_max-ans1)
        exit()
    n_max += 1
    print(n_max)


# while n_max > n_min+1:
#     n = (n_max + n_min)//2
#     xn = 0
#     for i, xx in enumerate(reversed(str_x)):
#         xn += int(xx)*(n**i)
#     print(f"{n_max} {n_min} xn{xn} m{m}")
#     if xn > m:
#         n_max = n
#     elif xn < m:
#         n_min = n
#     else:
#         n_max = n+1
#         break

print(n_max, ans1)
