import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

H, W, A, B = map(int, input().split())

def dps(pointer, fill, a, b):
    if pointer == H*W-1:
        return 1
    elif fill[pointer] == 1:
        return dps(pointer+1, fill, a, b)
    else:
        ans = 0
        if b > 0 and pointer < H*W:
            fill[pointer] = 1
            ans += dps(pointer, fill, a, b-1)
        if a > 0 and pointer+W < H*W:
            fill[pointer]



