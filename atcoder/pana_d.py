n = int(input())
s = [[] for i in range(n+1)]
s[1].append('a')
ans_s = []
for num in range(1,n):
    for st in s[num]:
        for add in range(97, max(map(ord,st))+2):
            s[num+1].append(st + chr(add))
for sw in s[n]:
    print(sw)