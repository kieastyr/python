import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, s, d = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        print("Yes")
        exit()
    
print("No")
