n = int(input())
a = list(map(int, input().split()))
if n%2 == 0:
    sum1 = 0
    sum2 = 0
    for i in range(n):
        if i%2 == 0:
            sum1 += a[i]
        else:
            sum2 += a[i]
    print(sum1 if sum1 > sum2 else sum2)
else:
    sum1 = [0, a[0]]
    sum2 = [a[1]]
    sum3 = [a[2]]
    max_sum = -1e10*n
    for i in range(1, n//2):
        sum1.append(sum1[i-1]+a[2*i])
    for i in range(1, n//2):
        sum2.append(sum2[i-1]+a[2*i+1])
    for i in range(1, n//2):
        sum3.append(sum3[i-1]+a[2*(i+1)])
    sum3.append(0)
    space1 = 0
    space2 = 0
    print(sum1, sum2, sum3)
    for space2 in range(n//2+1):
        for space1 in range(space2):
            sum4 = sum1[space1] + sum2[space2-1] - sum2[space1] + sum3[space2] - sum3[space2-1]
            if sum4 > max_sum:
                max_sum = sum4
    print(max_sum)

