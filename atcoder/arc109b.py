import sys
from decimal import Decimal
def input():
    return sys.stdin.readline()[:-1]

n = int(input())
m = 1

m = (int(Decimal(str(1+8*(n+1)))**Decimal('0.5')+Decimal("0.1"))-1)//2
print(n-m+1)

