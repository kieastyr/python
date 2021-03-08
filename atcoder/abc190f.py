import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a_list = list(map(int, input().split()))
count = [0 for _ in range(n)]
inv = [0 for _ in range(n)]
inv0 = 0
for i, a in enumerate(reversed(a_list)):
    inv[a] = sum(count[:a])
    count[a] += 1
    inv0 += inv[a]

print(inv0)
for i in range(n-1):
    inv0 += (n-1) - 2*a_list[i]
    print(inv0)
    # moved[a_list[i]] += 1
