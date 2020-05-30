n = int(input())
p_list = list(map(int, input().split()))
connect = {i: set() for i in range(1, n+1)}
undet = []
for i, p in enumerate(p_list):
    if p == -1:
        undet.append(i+1)
    else:
        connect[i+1].add(p)
        connect[p].add(i+1)

now_label = 0
label_count = {}
label_list = {i: 0 for i in range(1, n+1)}
unseen = n
while unseen > 0:
    now_label += 1
    label_count[now_label] = 0
    i = 1
    while i <= n and label_list[i] != 0:
        i += 1
    if i <= n:
        todo = [i]
        while len(todo) > 0:
            here = todo.pop(0)
            label_list[here] = now_label
            label_count[now_label] += 1
            unseen -= 1
            for next_i in connect[here]:
                if label_list[next_i] == 0:
                    todo.append(next_i)

ans = 0
for ud in undet:


