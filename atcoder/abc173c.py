h, w, k = map(int, input().split())
c = []
for _ in range(h):
    c.append(list(map(int, input().split())))
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

def nap(pi, rem, pos_i, neg_i, pos_max, neg_max):
    if rem == 0:
        return pi
    ans1 = 0
    ans2 = 0
    if pos_i + 2 < pos_max:
        tmp = pi * a_pos[pos_i] * a_pos[pos_i+1]
        ans1 = nap(tmp, rem-2, pos_i-2, neg_i, pos_max, neg_max)
    if neg_i + 2 < neg_max:
        tmp = pi * a_neg[neg_i] * a_pos[neg_i+1]
        ans2 = nap(tmp, rem-2, pos_i, neg_i-2, pos_max, neg_max)
    return max(ans1, ans2)

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
    if len(a_pos) >= k:
        ans1 = 1
        for i in range(k):
            ans1 *= a_pos[i]
            if ans1 > mod:
                ans1 %= mod
    else:
        ans1 = 0
    if k % 2 == 0:
        ans2 = 0
        for i in range(k):
            ans1 *= a_pos[i]
            if ans1 > mod:
                ans1 %= mod
