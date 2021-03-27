import sys
import math
from itertools import combinations
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
x0, y0 = list(map(int, input().split()))
xh, yh = list(map(int, input().split()))

xg = x0+xh
yg = y0+yh
# print(xg, yg)

x = x0*2-xg
y = y0*2-yg
theta = math.radians(360/n)

newx = x*math.cos(theta)-y*math.sin(theta)
newy = x*math.sin(theta)+y*math.cos(theta)

print(f"{(newx+xg)/2} {(newy+yg)/2}")