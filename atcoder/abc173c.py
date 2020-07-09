h, w, k = map(int, input().split())
c = []
w_count = []
h_count = [0 for _ in range(w)]
n = 0
for _ in range(h):
    tmp = list(input())
    for i in range(w):
        if tmp[i] == "#":
            h_count[i] += 1
    tc = tmp.count("#")
    n += tc
    w_count.append(tc)
    c.append(tmp)
# print(w_count, h_count)

ans = 0
for w_bin in range(2 ** w):
    for h_bin in range(2 ** h):
        w_bin_st = bin(w_bin)[2:].zfill(w)
        h_bin_st = bin(h_bin)[2:].zfill(h)
        # print(w_bin_st, h_bin_st)
        num = 0
        i_list = []
        j_list = []
        for i, wb in enumerate(list(w_bin_st)):
            if wb == "1":
                i_list.append(i)
                num += h_count[i]
        for j, hb in enumerate(list(h_bin_st)):
            if hb == "1":
                j_list.append(j)
                num += w_count[j]
        if n-num <= k:
            for il in i_list:
                for jl in j_list:
                    if c[jl][il] == "#":
                        num -= 1
            if n-num == k:
                # print(i_list, j_list)
                ans += 1

print(ans)