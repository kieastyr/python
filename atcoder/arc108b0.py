import sys
import random
def input():
    return sys.stdin.readline()

mod = int(1e9+7)

# h, w = 1000, 1000
# s = [["." for _ in range(w)] for _ in range(h)]

# import time
# t1 = time.time()

n = int(input())
s = input()
# n = 100000
# s = random.choices(["f", "o", "x"], k=n)
i = 0
# j = 0

fox_num = 0
while i < n-2:
    if s[i] == "f" and s[i+1] == "o" and s[i+2] == "x":
        fox_num += 1
        s = s[:i] + s[i+3:]
        # print(i, s)
        n -= 3
        i = max(i-3, -1)
    i += 1

# print(fox_num)
print(n)
