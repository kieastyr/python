import sys
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
num = [[0 for _ in range(w)] for _ in range(h)]

ans = 0
i = 0
j = 0
while s[i][j] == ".":
    j += 1
    if j == w:
        j = 0
        i += 1
si, sj = i, j
ans = 1

def right(si, sj, i, j, ans):
    # print(si, sj, i, j)
    while s[i][j] == "#" and s[i-1][j] == ".":
        j += 1
    if s[i][j] == ".":
        down(si, sj, i, j-1, ans+1)
    elif s[i-1][j] == "#":
        up(si, sj, i-1, j, ans+1)

def up(si, sj, i, j, ans):
    # print(si, sj, i, j)
    while s[i][j] == "#" and s[i][j-1] == ".":
        if i==si and j == sj:
            print(ans+1)
            exit()
        i -= 1
    if s[i][j] == ".":
        right(si, sj, i+1, j, ans+1)
    elif s[i][j-1] == "#":
        left(si, sj, i, j-1, ans+1)

def down(si, sj, i, j, ans):
    # print(si, sj, i, j)
    while s[i][j] == "#" and s[i][j+1] == ".":
        i += 1
    if s[i][j] == ".":
        left(si, sj, i-1, j, ans+1)
    elif s[i][j+1] == "#":
        right(si, sj, i, j+1, ans+1)

def left(si, sj, i, j, ans):
    # print(si, sj, i, j)
    while s[i][j] == "#" and s[i+1][j] == ".":
        if i == si and j == sj:
            print(ans+2)
            exit()
        j -= 1
    if s[i][j] == ".":
        up(si, sj, i, j+1, ans+1)
    elif s[i+1][j] == "#":
        down(si, sj, i+1, j, ans+1)

print(right(si,sj,si,sj, 0))