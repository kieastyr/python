x = int(input())
solved = [0 for _ in range(x+1)]
prime = [2, 3, 5]
sum1 = 0
for i in range(2, x+1):
    j = 0
    sum2 = i
    while prime[j]**2 <= i:
        count = 0
        while i % prime[j] == 0:
            i //= prime[j]
            count += 1
        sum2 *= count+1
        j += 1
    if sum2 == i:
        prime.append(i)
        sum2 *= 2
    sum1 += sum2
print(sum1+1)