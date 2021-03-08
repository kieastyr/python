import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n, k = map(int, input().split())
ans = n
for i in range(k):
    a1 = sorted(list(str(ans)))
    print(a1)
    ans = int("".join(reversed(a1))) - int("".join(a1))
    
print(ans)

