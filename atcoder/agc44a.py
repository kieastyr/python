# t = int(input())
# for _ in range(t):
n, a, b, c, d = map(int, input().split())
tree = {n: {"cost": 0, "from": None}}
# route = []
# now_node = 0
# if n < 5:
#     max_n = 10
# else:
#     max_n = 2*n

mods = [2, 3, 5]
costs = [a, b, c]


def search(now_num, tree):
    print(tree)
    if now_num == 1:
        return tree[now_num]["cost"] + d
    total_cost = [1e10]
    for mod, cost in zip(mods, costs):
        if now_num % mod == 0:
            if tree.get(now_num // mod) is None:
                tree[now_num // mod] = {"cost": tree[now_num]["cost"] + cost, "from": now_num}
                total_cost.append(search(now_num//mod, tree))
            elif tree[now_num // mod]["cost"] > tree[now_num // mod]["cost"]:
                tree[now_num // mod]["cost"] = tree[now_num // mod]["cost"]
                tree[now_num // mod]["from"] = now_num
                total_cost.append(search(now_num//mod, tree))
    if len(total_cost) == 1:
        for dis in [1, -1]:
            if tree.get(now_num+dis) is None:
                tree[now_num+dis] = {"cost": tree[now_num]["cost"] + d, "from": now_num}
                total_cost.append(search(now_num+dis, tree))
            elif tree[now_num+dis]["cost"] > tree[now_num]["cost"] + d:
                tree[now_num+dis]["cost"] = tree[now_num]["cost"] + d
                tree[now_num+dis]["from"] = now_num
                total_cost.append(search(now_num+dis, tree))

    return min(total_cost)


print(search(n, tree))
