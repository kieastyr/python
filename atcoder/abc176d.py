h, w = map(int, input().split())
ch, cw = map(int, input().split())
dh, dw = map(int, input().split())
ch -= 1
cw -= 1
dh -= 1
dw -= 1

s = [list(input()) for _ in range(h)]
floor = 0
s[ch][cw] = str(floor)
deque = {0: {ch*w+cw}}

def search(i, j):
    for n in range(25):
        h1 = i+n//5-2
        w1 = j+n%5-2
        if 0 <= h1 < h and 0 <= w1 < w:
            if s[h1][w1] == '.':
                s[h1][w1] = str(floor+1)
                deque[floor+1].add(h1*w+w1)
    
    for hn, wn in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        h1 = i+hn
        w1 = j+wn
        if 0 <= h1 < h and 0 <= w1 < w:
            if s[h1][w1] == '.':
                s[h1][w1] = str(floor)
                deque[floor].add(h1*w+w1)
            elif s[h1][w1] == str(floor+1):
                deque[floor+1].discard(h1*w+w1)
                s[h1][w1] = str(floor)
                deque[floor].add(h1*w+w1)

while s[dh][dw] == '.':
    if len(deque[floor]) == 0:
        s[dh][dw] = -1
        break
    
    deque[floor+1] = set()
    while len(deque[floor]):
        n = deque[floor].pop()
        search(n//w, n%w)
    # print(s)
    floor += 1

print(s[dh][dw])
