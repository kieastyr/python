import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, m = map(int, input().split())
a_list, b_list = [], []
for _ in range(m):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

k = int(input())
c_list, d_list = [], []
for _ in range(k):
    c, d = map(int, input().split())
    c_list.append(c)
    d_list.append(d)

ans = 0
for i in range(2**k):
    dish = [0 for _ in range(n+1)]
    for j in range(k):
        if (i >> j) & 1 == 0:
            dish[c_list[j]] += 1
        else:
            dish[d_list[j]] += 1
    num = 0
    print(dish)
    for j in range(m):
        if dish[a_list[j]] * dish[b_list[j]] >= 1:
            num += 1
    ans = max(ans, num)
print(ans)
