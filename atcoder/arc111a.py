import sys
def input():
    return sys.stdin.readline()[:-1]

n, m = map(int, input().split())
print(pow(10, n, m * m) // m % m)