

import sys
def input():
    return sys.stdin.readline()

mod = int(1e9+7)

# h, w = 1000, 1000
# s = [["." for _ in range(w)] for _ in range(h)]

# import time
# t1 = time.time()

s, p = map(int, input().split())
i = 1
while i*i <= p:
    if p % i == 0 and i + p //i == s:
        print("Yes")
        exit()
    i += 1

print("No")
