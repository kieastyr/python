# n = 100000
# a = [random.randint(1, 1000000000) for _ in range(n)]
n, m = map(int, input().split())
w = sorted(list(map(int, input().split())), reverse=True)
lv = []

min_v = 1e8+1
l_min_v = 0
for _ in range(m):
    l, v = map(int, input().split())
    if v < min_v:
        min_v = v
        l_min_v = l
    lv.append([l, v])

# print(f"min_v:{min_v}")
if min_v < w[0]:
    print(-1)
else:
    w_new = []
    j = n-1
    while len(w) > 0 and w[0] + w[j] > min_v:
        w_new.append(w.pop(0))
        j -= 1
    if len(w) == 1:
        w_new.append(w.pop(0))
    elif len(w) >= 2:
        while len(w) >= 2:
            i = 0
            j = len(w)-1
            flag = -1
            while i < j and w[i] + w[j] <= min_v:
                if flag == 0 or flag == -1:
                    i += 1
                    flag = 1
                elif flag == 1:
                    j -= 1
                    flag = 0
            if i <= j:
                if flag == -1:
                    w_new.append(w.pop(i))
                elif flag == 0:
                    w[i] += w.pop(j+1)
                elif flag == 1:
                    w[i-1] += w.pop(j)
            else:
                w_new.extend(w)
                break
        if len(w) == 1:
            w_new.append(w[0])
    
    print(w_new)
    # lv = sorted(lv, reverse=True, key=lambda x:x[0])
    w_new_s = sorted(w_new, reverse=True)

    for l, v in lv:
        if l > l_min_v and v < w_new_s[0] + w_new_s[1]:
            print(l)
            l_min_v = l

    print((len(w_new)-1)*l_min_v)
