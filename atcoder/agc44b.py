n = int(input())
ps = list(map(int, input().split()))
rem_num = {}

for i in range(1, n*n+1):
    rem_num[i] = min([(i-1)//n, n - (i-1)//n - 1, (i-1) % n, n - (i-1) % n - 1])


ans = 0
for p in ps:
    print(f"{p} {rem_num} {rem_num[p]}")
    ans += rem_num[p]
    queue = [p]
    # if p - n > 0 and rem_num[p] < rem_num[p-n]:
    #     queue.append(p-n)
    #     rem_num[p - n] = rem_num[p]
    # if p + n < n*n+1 and rem_num[p] < rem_num[p+n]:
    #     queue.append(p+n)
    #     rem_num[p + n] = rem_num[p]
    # if p % n != 1 and rem_num[p] < rem_num[p-1]:
    #     queue.append(p-1)
    #     rem_num[p - 1] = rem_num[p]
    # if p % n != 0 and rem_num[p] < rem_num[p+1]:
    #     queue.append(p+1)
    #     rem_num[p + 1] = rem_num[p]
    rem_num[p] -= 1

    while len(queue) > 0:
        q = queue.pop(0)
        if q - n > 0 and rem_num[q] + 1 < rem_num[q-n]:
            queue.append(q-n)
            rem_num[q - n] = rem_num[q]
        if q + n < n*n+1 and rem_num[q] + 1 < rem_num[q+n]:
            queue.append(q+n)
            rem_num[q + n] = rem_num[q]
        if q % n != 1 and rem_num[q] + 1 < rem_num[q-1]:
            queue.append(q-1)
            rem_num[q - 1] = rem_num[q]
        if q % n != 0 and rem_num[q] + 1 < rem_num[q+1]:
            queue.append(q+1)
            rem_num[q + 1] = rem_num[q]

print(ans)
