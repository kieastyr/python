n, k, c = map(int, input().split())
s = " " + input()
work_fw = [0]*k
work_bw = [0]*k
i = 1
now_k = 0
while i <= n and now_k < k:
    if s[i] == 'o':
        work_fw[now_k] = i
        now_k += 1
        i += c
    i += 1
if now_k != k:
    print("")
else:
    i = n
    now_k = k - 1
    while i > 0 and now_k >= 0:
        if s[i] == 'o':
            work_bw[now_k] = i
            now_k -= 1
            i -= c
        i -= 1
    # print(work_fw)
    # print(work_bw)
    for i in range(k):
        if work_fw[i] == work_bw[i]:
            print(work_fw[i] )
