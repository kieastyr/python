n = int(input())
s = input()
r = 0
sum_rgb = 0
def_count = 0
b_count = []
while r < n and s[r] != 'R':
    r += 1
for b in range(r+2, n):
    for g in range(r+1, b):
        if s[g] == 'G' and s[b] == 'B':
            def_count += 1
b = n-1
while b > r and s[b] != 'B':
    b -= 1
i = 1
while i < n and s[i] != 'G':
    i += 1
i += 1
b_num = 0
while i < n:
    if s[i] == 'B':
        b_num += 1
    elif s[i] == 'G':
        b_count.append(b_num)
        b_num = 0
    i += 1
b_count.append(0)
print(def_count, b_count)

g_place = 0
while r < b:
    print(r, g, b)
    if (b+r)%2 == 0 and s[(b+r)//2]=='G':
        sum_rgb += def_count-1
    else:
        sum_rgb += def_count
    r += 1
    while r < b and s[r] != 'R':
        if s[r] == 'G':
            def_count -= b_count[g_place]
            g_place += 1
        r += 1

print(sum_rgb)