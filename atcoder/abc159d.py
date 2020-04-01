n = int(input())
a = [0]
a.extend(list(map(int, input().split())))
max_a = max(a)
counter = [0]*(max_a+1)
combi_common = 0
for num in a:
    counter[num] += 1
for i in range(1, max_a+1):
    if counter[i] >= 2:
        combi_common += counter[i]*(counter[i]-1)//2
for j in range(1,n+1):
    cou = counter[a[j]]
    if cou >= 2:
        out = combi_common + ((cou-1)*(cou-2) - cou*(cou-1))//2
    else:
        out = combi_common
    print(out)