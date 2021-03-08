import sys
def input():
    return sys.stdin.readline()[:-1]

mod = int(1e9+7)

a, b = map(int, input().split())
c, d = map(int, input().split())

if a==c and b==d:
    print(0)
elif a+b == c+d or a-b == c-d or abs(a-c)+abs(b-d) <= 3:
    print(1)
elif (a-c+b-d)%2 == 0 or abs((a+b)-(c+d)) <= 3 or abs((a-b)-(c-d)) <= 3:
    print(2)
else:
    print(3)
