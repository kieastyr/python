k = int(input())
ans = 0
now = 7
if k == 1 or k == 7:
    now = 0
while True:
    if ans > k:
        print(-1)
        break
    elif now == 0:
        print(ans+1)
        break
    else:
        now = (now*10 + 7) % k
        ans += 1