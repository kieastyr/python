import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
a_max = int(math.sqrt(n))+1
# print(a_max)
ans = n
a_dict = {i: 1 for i in range(2, a_max+1)}

d = a_max+1
a = 2
while a < d:
    v = a_dict[a]
    if v == 1:
        aa = a*a
        while aa <= n:
            if aa < a_max and a_dict[aa] == 1:
                a_dict[aa] -= 1
            ans -= 1
            aa *= a
    a += 1

print(ans)
        
