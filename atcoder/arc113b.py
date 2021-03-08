import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
a, b, c = map(int, input().split())
# print(a, b, c)
a %= 10
count = 1
a_pow = a*a%10
a_pow_list = [a]
while a != a_pow:
    a_pow_list.append(a_pow)
    a_pow *= a
    a_pow %= 10
    count += 1
# print(a_pow_list)
print(a_pow_list[pow(b, c, count)-1])
