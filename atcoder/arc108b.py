import sys
def input():
    return sys.stdin.readline()

mod = int(1e9+7)

# h, w = 1000, 1000
# s = [["." for _ in range(w)] for _ in range(h)]

# import time
# t1 = time.time()

n = int(input())
s = input()

f_lank = 0
o_lank = 0
x_lank = 0
fox_num = 0
for i in range(n):
    if s[i] == "f":
        f_lank += 1
    elif s[i] == "o" and f_lank > o_lank:
        o_lank += 1
    elif s[i] == "x" and o_lank > x_lank:
        x_lank += 1

# print(fox_num)
print(n-3*x_lank)
