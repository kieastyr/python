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
c_pir = [["" for j in range(n-i)] for i in range(1, n)]
c_pir.insert(0, list(input()))
print(c_pir)
next_dict = {}

now = c_pir[0][:2]
next = color(now[0], now[1])
next_dict[now[0]][now[1]]["E"] = next

