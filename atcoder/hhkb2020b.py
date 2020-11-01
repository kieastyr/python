h, w = map(int, input().split())
s = []
ans = 0

for _ in range(h):
    s.append(input())

for i in range(h):    
    for j in range(1, w):
        if s[i][j] == '.':
            if s[i][j-1] == '.':
                ans += 1
            if i != 0 and s[i-1][j] == '.':
                ans += 1

print(ans)
