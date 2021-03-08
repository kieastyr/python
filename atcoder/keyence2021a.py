import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

now_a = a[0]
now_b = b[0]
max_a = 0
for i in range(n):
    if now_a*now_b < max_a*b[i]:
        now_a = max_a
        now_b = b[i]
    elif now_a*now_b < a[i]*b[i]:
        now_a = a[i]
        now_b = b[i]
    elif now_b < b[i]:
        now_b = b[i]
    max_a = max(max_a, a[i])
    
    print(now_a*now_b)