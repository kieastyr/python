mod = int(10e9+7)
n, k = map(int, input().split())
a_list = list(map(int, input().split()))
a_pos = []
a_neg = []
zero_count = 0
for a in a_list:
    if a > 0:
        a_pos.append(a)
    elif a < 0:
        a_neg.append(a)
    else:
        zero_count += 1

if len(a_pos) == 0 and k % 2 == 1:
    if zero_count > 0:
        print(0)
    else:
        ans = 1
        a_neg.sort()
        for i in range(k):
            ans *= a_neg[i]
            if ans > mod:
                ans %= mod
        print(ans)
else:
    a_pos.sort(reverse=True)
    a_neg.sort()
    if k % 2 == 1:
        ans = a_pos.pop(0)
        k -= 1
    else:
        ans = 1
    dig = 0
    i = 0
    while i < len(a_pos)-1 and i < k:
        for _ in range(2):
            ans *= a_pos[i]
            if ans > mod:
                ans //= mod
                dig += 9
            i += 1
    max_i = i-1
    while i < k-1:
        ans *= a_neg[i]
        if ans < -mod:
            ans //= mod
            dig += 9
        i += 1
        ans *= a_neg[i]
        if ans > mod:
            ans //= mod
            dig += 9
        i += 1
    max_j = i - 1
    max_dig = dig
    while max_j >= 0 and max_i >= 0:
        