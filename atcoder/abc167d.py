n, k = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
# print(a)
if a[1] == 1:
    print(1)
else:
    reached = {i: 0 for i in range(1, n+1)}
    now = 1
    count = 0
    while reached[now] == 0:
        reached[now] = count
        now = a[now]
        count += 1
    roop = count - reached[now]
    if k < reached[now]:
        index = k
    else:
        index = (k - reached[now]) % roop + reached[now]
    # print(reached, count)
    # print(roop, index)
    for key, value in reached.items():
        if value == index:
            print(key)
            break

