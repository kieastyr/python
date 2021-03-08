import sys
def input():
    return sys.stdin.readline()[:-1]

prime = []
i = 2
j = 2
while i < 10000:
    while j*j <= i:
        if i%j == 0:
            break
        j += 1
    if j*j > i:
        prime.append(i)
    i += 1
    j = 2

n = len(prime)
print(n)
for i in prime[:100]:
    for j in prime[i+1:101]:
        for k in prime[j+1:102]:
            r = i+j
            p = j*k
            s = k*i
            print(i, j, k)
            print(r, p, s)
            for l in range(2*((k+1)//2), max(r, p, s), 2):
                if r%l == i and p%l == j and s%l == k:
                    print("find!!")
                    print(i, j, k, l)
                    exit()
                if r%l == j and p%l == k and s%l == i:
                    print("find!!")
                    print(i, j, k, l)
                    exit()


