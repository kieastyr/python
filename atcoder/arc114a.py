import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

def gcd(a, b):
    if a < b:
        c = a
        a = b
        b = c
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

n = int(input())
x_list = list(map(int, input().split()))
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
# primes = [2, 3, 5, 7]
ans = 1
for i in primes:
    ans *= i

for i in range(1, 2**len(primes)):
    now = 1
    for j in range(len(primes)):
        if (i>>j) & 1 == 1:
            now *= primes[j]
    flag = 1
    for x in x_list:
        if gcd(now, x) == 1:
            flag = 0
            break
    
    if flag:
        ans = min(ans, now)

print(ans)
