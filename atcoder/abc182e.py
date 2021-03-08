import sys
def input():
    return sys.stdin.readline()[:-1]

h, w, n, m = map(int, input().split())
field = [[0 for j in range(w)] for i in range(h)]
light = []
block = []
for i in range(n):
    a, b = map(int, input().split())
    light.append((a-1, b-1))
for i in range(m):
    a, b = map(int, input().split())
    field[a-1][b-1] = -1
    block.append((a-1, b-1))
    
for num in range(n):
    i, j = light[num]
    if field[i][j] != 1:
        field[i][j] = 1
        jj = j-1
        while jj >= 0 and field[i][jj] != -1:
            field[i][jj] = 1
            jj -= 1
        jj = j+1
        while jj < w and field[i][jj] != -1:
            field[i][jj] = 1
            jj += 1

for num in range(n):
    i, j = light[num]
    if field[i][j] != 2:
        field[i][j] = 2
        ii = i-1
        while ii >= 0 and field[ii][j] != -1:
            field[ii][j] = 1
            ii -= 1
        ii = i+1
        while ii < h and field[ii][j] != -1:
            field[ii][j] = 2
            ii += 1

print(sum(field[i].count(1) for i in range(h))+sum(field[i].count(2) for i in range(h)))