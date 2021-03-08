import sys
def input():
    return sys.stdin.readline()[:-1]

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
sum_a = 0
min_a = 100
for i in range(h):
    sum_a += sum(a[i])
    min_a = min(a[i]+[min_a])

print(sum_a-(min_a*h*w))
