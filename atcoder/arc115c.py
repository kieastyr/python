import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

primes = []

def pf(n):
    max_beki = 0
    ans = {}
    n_copy = n
    for p in primes:
        if n_copy == 1:
            break
        if n_copy%p == 0:
            ans[p] = 1
            n_copy //= p
            while n_copy%p == 0:
                ans[p] += 1
                n_copy //= p
            max_beki += ans[p]
    
    if n_copy == n:
        primes.append(n)
        return 1
    else:
        return max_beki

n = int(input())
print(1, end=" ")
for i in range(2, n+1):
    print(pf(i)+1, end=' ')
    # print(pf(i))

print("")


        
        

