def nap(abcd, i, array, score, m, q):
    if i == q:
        up = n
        bottom = 1
        while array[up] == 0:
            up -= 1
        while array[bottom] == 0:
            bottom += 1
        if array[up] - array[bottom] >= m:
            return -1
        else:
            return score
    else:
        a, b, c, d = abcd[i]
        if array[a] == 0 or array[a] == array[b] - c:
            array[a] = array[b] - c
            score2 = nap(abcd, i+1, array, score+d, m, q)
        else:
            score2 = nap(abcd, i+1, array, score, m, q)
        if array[b] == 0 or array[b] == array[a] + c:
            array[b] = array[a] + c
            score1 = nap(abcd, i+1, array, score+d, m, q)
        else:
            score1 = nap(abcd, i+1, array, score, m, q)

        if score1 > score2:
            return score1
        else:
            return score2


n, m, q = map(int, input().split())
abcd = []
array = [0 for _ in range(n+1)]
for i in range(q):
    abcd.append(tuple(map(int, input().split())))
abcd.sort(reverse=True, key=lambda temp: temp[3])
print(nap(abcd, 0, array, 0, m, q))
