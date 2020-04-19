k = int(input())
def gcd(a, b, c):
    gcd1 = 1
    if a%c == 0 and b%c == 0:
        gcd1 = c
    elif a%2 == 0 and b%2 == 0 and c%2 == 0:
        gcd1 = 2
        for i in range(4, c//2+1, 2):
            if a%i == 0 and b%i == 0 and c%i == 0:
                gcd1 = i
    else:
        for i in range(3, c//2+1, 2):
            if a%i == 0 and b%i == 0 and c%i == 0:
                gcd1 = i
    # print(gcd1)
    return gcd1

sum_gcd = 0
for a in range(1, k+1):
    for b in range(1, a+1):
        for c in range(1, b+1):
            if a == b and b == c:
                sum_gcd += gcd(a, b, c)
            elif a == b or b == c or c == a:
                sum_gcd += 3*gcd(a, b, c)
            else:
                sum_gcd += 6*gcd(a, b, c)
print(sum_gcd)
