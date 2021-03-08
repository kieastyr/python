import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

a, b, c = map(int, input().split())
if a > b:
    print("Takahashi")
elif b > a or c == 0:
    print("Aoki")
else:
    print("Takahashi")
