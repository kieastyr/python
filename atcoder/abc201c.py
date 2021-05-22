import sys
import math

def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

s = input()
if s.count('o') > 4 or s.count('x') == 10:
    print(0)
else:
    if s.count('o') == 4:
        print(4*3*2)
    elif s.count('o') == 3:
        n1 = 4*3*2*s.count('?')
        n2 = 3*4*3*2//2
        print(n1+n2)
    elif s.count('o') == 2:
        n1 = 6*2*s.count('?')*s.count('?')
        n2 = 2*4*3*2//2*s.count('?')
        n3 = 4*3*2//2//2
        n4 = 2*4
        print(n1+n2+n3+n4)
    elif s.count('o') == 1:
        n1 = 4*s.count('?')*s.count('?')*s.count('?')
        n2 = 6*s.count('?')*s.count('?')
        n3 = 4*s.count('?')
        n4 = 1
        print(n1+n2+n3+n4)
    else:
        print(s.count('?')**4)

