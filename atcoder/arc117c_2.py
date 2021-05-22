import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

def color(i, j):
    if i == j:
        return i
    elif i == "B":
        if j == "W":
            return "R"
        else:
            return "W"
    elif i == "W":
        if j == "B":
            return "R"
        else:
            return "B"
    else:
        if j == "B":
            return "W" 
        else:
            return "B"


n = int(input())
c_pir = [["" for j in range(n-i)] for i in range(2, n, 2)]
c_pir.insert(0, list(input()))
next_dict = {}

for i in ["B", "W", "R"]:
    next_dict[i] = {}
    for j in ["B", "W", "R"]:
        next_dict[i][j] = {}
        for k in ["B", "W", "R"]:
            next_dict[i][j][k] = color(color(i, j), color(j, k))

# print(next_dict)

for i, l in enumerate(range(n, 0, -2)):
    if i > 0:
        for j in range(l):
            c_pir[i][j] = next_dict[c_pir[i-1][j]][c_pir[i-1][j+1]][c_pir[i-1][j+2]]

if len(c_pir[-1]) == 2:
    print(color(c_pir[-1][0], c_pir[-1][1]))
else:
    print(c_pir[-1][0])