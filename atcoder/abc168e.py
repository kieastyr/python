mod = 1000000007
n = int(input())
score_set = set()
counter = {}
for _ in range(n):
    i, j = map(int, input().split())
    score = i*j
    if score in score_set:
        counter[score][0] += 1
    elif -score in score_set:
        counter[-score][1] += 1
    else:
        counter[score] = [1, 0]
    score_set.add(score)

print(counter)

dim = 0
for a, b in counter.items():
    if a >= 1 and b >= 1:
       dim +=

combi = 1
for i in range(n):
    combi *= 2

