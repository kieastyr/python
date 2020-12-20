import csv
import random

node_num = 1000
edge_num = 10000

member = list(range(node_num))
edge = []
for i in range(edge_num):
    a, b = random.sample(member, 2)
    if random.random() < 0.3:
        a = "ALL"
    if all([x[:2] != [a, b] for x in edge]):
        edge.append([a, b, random.randint(1, 100)*100])
edge = [list(x) for x in zip(*edge)]
member.insert(0, "MEMBER")
edge[0].insert(0, "FROM")
edge[1].insert(0, "TO")
edge[2].insert(0, "")

with open("test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(member)
    writer.writerow(edge[0])
    writer.writerow(edge[1])
    writer.writerow(edge[2])
