import sys
def input():
    return sys.stdin.readline()[:-1]

mod = int(1e9+7)

n, x = map(int, input().split())
s = input()

for i in s:
    if i == "o":
        x += 1
    elif i == "x":
        if x > 0:
            x -= 1

print(x)
