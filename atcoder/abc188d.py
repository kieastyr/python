import sys
def input():
    return sys.stdin.readline()[:-1]

n, c = map(int, input().split())
imosu = {0: 0}

for i in range(n):
    a1, b1, c1 = map(int, input().split())
    if imosu.get(a1):
        imosu[a1] += c1
    else:
        imosu[a1] = c1
    if imosu.get(b1+1):
        imosu[b1+1] -= c1
    else:
        imosu[b1+1] = -c1

imosu_s = sorted(imosu.items(), key=lambda x: x[0])

ans = 0
prev_day = 0
prev_money = 0
for i, (day, money) in enumerate(imosu_s):
    money += prev_money
    if prev_money < c:
        ans += prev_money*(day-prev_day)
    else:
        ans += c*(day-prev_day)
    prev_day = day
    prev_money = money

print(ans)