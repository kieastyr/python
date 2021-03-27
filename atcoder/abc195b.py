import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

a, b, w = map(int, input().split())
if w*1000//a == w*1000//b and (w*1000)%a!=0 and (w*1000)%b!=0:
    print("UNSATISFIABLE")
else:
    print(f"{(w*1000-1)//b+1} {w*1000//a}")

