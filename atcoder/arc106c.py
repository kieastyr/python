n, m = map(int, input().split())
seg = []
if m < 0 or (m >= n-1 and n != 1):
    print(-1)
else:
    if m == 0:
        for i in range(n):
            seg.append([2*i+1, 2*i+2])
    else:
        for i in range(m+1):
            seg.append([2*i+2, 2*i+3])
        seg.append([1, 2*m+6])
        for i in range(n-m-2):
            seg.append([2*m+2*i+7, 2*m+2*i+8])

    for lr in seg:
        print(f"{lr[0]} {lr[1]}")
