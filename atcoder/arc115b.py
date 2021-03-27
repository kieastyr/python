import sys
import math
import numpy as np
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a_min = []
diag = []
ident = np.ones(n, dtype=np.int)
c = np.zeros((n, n), dtype=np.int)
for i in range(n):
    cc = list(map(int, input().split()))
    c[i] = np.array(cc) 
    diag.append(cc[i])
    cc_min = np.min(cc)
    a_min.append(cc_min)

b_min = np.min(c, axis=0).tolist()

# print(a_min, b_min)

for i in range(n):
    d = min(map(lambda x, y: a_min[i]+x-y, b_min, c[i]))
    if d < 0:
        print("No")
        exit()
    else:
        # print(i+1, d)
        a_min[i] -= d

for i in range(n):
    d = min(map(lambda x, y: b_min[i]+x-y, a_min, c[:, i]))
    if d < 0:
        print("No")
        exit()
    else:
        # print(i+1, d)
        b_min[i] -= d

for i in range(n):
    d = list(map(lambda x, y: a_min[i]+x-y, b_min, c[i]))
    for dd in d:
        if dd != 0:
            print("No")
            exit()

for i in range(n):
    d = list(map(lambda x, y: b_min[i]+x-y, a_min, c[: ,i]))
    for dd in d:
        if dd != 0:
            print("No")
            exit()

print("Yes")
print(" ".join(list(map(str, a_min))))
print(" ".join(list(map(str, b_min))))

