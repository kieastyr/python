n, m = map(int, input().split())
center1 = (m+1) // 2
center2 = center1 + m
for i in range(m):
    if i % 2 == 0:
        a = center1 - i // 2
        b = center1 + i // 2 + 1
    else:
        a = center2 - i // 2
        b = center2 + (i+1) // 2 + 1
    print(f"{a} {b}")
