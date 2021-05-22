import sys
import math

def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

n = int(input())
mount = {}
for _ in range(n):
    k, v = input().split()
    mount[k] = int(v)

mount_sort = sorted(mount.items(), key=lambda x: x[1], reverse=True)
print(mount_sort[1][0])

