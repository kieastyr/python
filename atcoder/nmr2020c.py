n = int(input())
a_list = list(map(int, input().split()))

flag = 0
node_sum = 0
now_node = 0
max_node = [1]
for i in range(1, n+1):
    max_node.append((max_node[i-1]-a_list[i-1])*2)
# print(max_node)

for d, a in enumerate(reversed(a_list)):
    d = n-d
    max_now = max_node[d]
    if (now_node+1)//2 + a > max_now:
        flag = 1
        break
    elif now_node + a > max_now:
        now_node = max_now
    else:
        now_node += a
    node_sum += now_node
    # print(f"{d} {now_node}")

if flag == 1:
    print(-1)
else:
    print(node_sum)
