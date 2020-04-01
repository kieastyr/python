h, w, k = list(map(int, input().split()))
choco = []
for _ in range(h):
    ip = list(map(int, list(input())))
    choco.append(ip)
# print(choco)
h_cut = [True]*(h-1)
h_cut.append(False)
min_cut = w*h
while sum(h_cut) < h:
    cut_index = []
    flag = 0
    for i in range(h-1):
        if h_cut[i]:
            if flag == 0:
                h_cut[i] = False
                if not h_cut[i+1]:
                    h_cut[i+1] = True
                    flag = 1
            else:
                cut_index.append(i+1)
        else:
            if flag == 0:
                h_cut[i] = True
                flag = 1
                cut_index.append(i+1)
    cut_index.append(h)
    now_cut = len(cut_index)-1
    w_from = 0
    w_to = 1
    while w_to <= w:
        h_from = 0
        for h_i in cut_index:
            # print([l[w_from:w_to] for l in choco[h_from:h_i]], h_from, h_i, w_from, w_to)
            if sum(map(sum, [l[w_from:w_to] for l in choco[h_from:h_i]])) > k:
                if w_to - w_from == 1:
                    w_to = w
                    now_cut += w*h
                    break
                else:
                    now_cut += 1
                    w_from = w_to-1
            else:
                h_from = h_i
                w_to += 1
    if now_cut < min_cut:
        min_cut = now_cut
print(min_cut)
