import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

n = int(input())
num = 0
i = 1
num = set()
while i*i <= n:
    if n%i == 0:
        if i%2 == 1:
            num.add(i)
        if n//i%2 == 1:
            num.add(n//i)
    i += 1
# num.add(n)
print(len(num)*2)
