import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, x = map(int, input().split())
a_list = list(map(int, input().split()))

for a in a_list:
    if a != x:
        print(a, end=" ")
