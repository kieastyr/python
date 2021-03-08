import sys
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
a = list(map(int, input().split()))

a1_max = 0
for i in range(2**(n-1)):
    if a[i] > a[a1_max]:
        a1_max = i
a2_max = 2**(n-1)
for i in range(2**(n-1), 2**n):
    if a[i] > a[a2_max]:
        a2_max = i

if a[a1_max] < a[a2_max]:
    print(a1_max+1)
else:
    print(a2_max+1)