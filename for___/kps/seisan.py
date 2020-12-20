from graphviz import Digraph
import csv
import time

t1 = time.time()

name_set = set()
bef_g = Digraph(format="png")
aft_g = Digraph(format="png")
ft_dict = {"FROM": [], "TO": []}
money_dict = {}

with open("hakone.csv", "r") as f:
    reader = csv.reader(f)
    for line in reader:
        if len(line) > 0:
            if line[0] == "MEMBER":
                # make name list
                for name in line[1:]:
                    if name != '':
                        name_set.add(name)
                        bef_g.node(name)
            elif line[0] == "TO" or line[0] == "FROM":
                # input keys as "FROM>TO"
                for name in line[1:]:
                    if "," in name:
                        name_list = name.replace(" ", "").split(",")
                        for n in name_list:
                            ft_dict[line[0]].append(name)

                    # append from-to names
                    ft_dict[line[0]].append(name)
            else:
                # input values as int
                for i, price in enumerate(line[1:]):
                    if price != '':
                        money_key = ft_dict["FROM"][i] + ">" + ft_dict["TO"][i]
                        if '*' in price:
                            unit, num = map(int, price.split("*"))
                            price_int = unit*len(name_set)
                            print(unit, price_int)
                        else:
                            price_int = int(price)
                        if money_dict.get(money_key):
                            money_dict[money_key] += price_int
                        else:
                            money_dict[money_key] = price_int

print(name_set)
print(money_dict)
# divide money of "ALL"
for f, t in zip(ft_dict["FROM"], ft_dict["TO"]):
    if f == "ALL":
        num = len(name_set)
        price = round(money_dict.pop(f+">"+t)/num)
        for name in name_set:
            if name != t:
                if money_dict.get(name + ">" + t):
                    money_dict[name + ">" + t] += price
                else:
                    money_dict[name + ">" + t] = price

# construct before_graph
edge = dict(zip(name_set, [[] for _ in range(len(name_set))]))
for ft, price in money_dict.items():
    f, t = ft.split(">")
    edge[f].append(t)
    bef_g.edge(f, t, label=str(price))


# remove cycle
def rem_cycle(f, t_list, money_dict):
    while len(t_list) > 0:
        # print(money_dict)
        # print(f, t_list)
        t = t_list.pop(0)
        if len(edge[t]) > 0:
            for t_t in name_set:
                if money_dict.get(f+">"+t) and money_dict.get(t+">"+t_t):
                    m1 = money_dict[f+">"+t]
                    m2 = money_dict[t+">"+t_t]
                    # new f -> t_t
                    new_price = min(m1, m2)
                    if m1 > m2:
                        money_dict[f + ">" + t] -= money_dict.pop(t + ">" + t_t)
                    elif m1 == m2:
                        money_dict.pop(f + ">" + t)
                        money_dict.pop(t + ">" + t_t)
                    else:
                        money_dict[t + ">" + t_t] -= money_dict.pop(f + ">" + t)

                    if t_t != f:
                        t_list.append(t_t)
                        if money_dict.get(f + ">" + t_t):
                            money_dict[f+">"+t_t] += new_price
                        else:
                            money_dict[f + ">" + t_t] = new_price
    return money_dict


for f in name_set:
    money_dict = rem_cycle(f, list(name_set-set(f)), money_dict)
print(money_dict)

# construct after_graph
for ft, price in money_dict.items():
    f, t = ft.split(">")
    aft_g.edge(f, t, label=str(price))

print(time.time()-t1)
bef_g.render("before", view=True)
aft_g.render("after", view=True)
