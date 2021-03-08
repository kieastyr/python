import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
eps = 0.9
intize = 10000

X, Y, R = map(float, input().split())
Xi = int(X*intize)
Yi = int(Y*intize)
Ri = int(R*intize)
r2 = Ri*Ri
y = (Yi-Ri)//intize*intize-intize

x_pre1 = math.floor(X)*intize
x_pre2 = math.ceil(X)*intize
if x_pre1 == x_pre2:
    x_pre2 += intize

count1 = 0
count2 = 0
ans = 0
while y <= Yi:
    x1 = x_pre1
    x2 = x_pre2
    while (x1-Xi)**2 + (y-Yi)**2 <= r2+eps:
        x1 -= intize
        count1 += 1
    while (x2-Xi)**2 + (y-Yi)**2 <= r2+eps:
        x2 += intize
        count2 += 1
    x_pre1 = x1
    x_pre2 = x2
    ans += (count1 + count2)
    # print(y, count1, count2)
    y += intize


y = (Yi+Ri)//intize*intize+intize
x_pre1 = math.floor(X)*intize
x_pre2 = math.ceil(X)*intize
count1 = 0
count2 = 0
if x_pre1 == x_pre2:
    x_pre2 += intize

while y > Yi:
    x1 = x_pre1
    x2 = x_pre2
    while (x1-Xi)**2 + (y-Yi)**2 <= r2+eps:
        x1 -= intize
        count1 += 1
    while (x2-Xi)**2 + (y-Yi)**2 <= r2+eps:
        x2 += intize
        count2 += 1
    x_pre1 = x1
    x_pre2 = x2
    ans += (count1 + count2)
    # print(y, count1, count2)
    y -= intize

print(ans)

