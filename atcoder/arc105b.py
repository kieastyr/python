# import random
def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

a_dict = {}
n = int(input())
# n = 100000
# a = [random.randint(1, 1000000000) for _ in range(n)]
a = list(map(int, input().split()))
min_a = min(a)

ans = min_a
for i in range(n):
    a[i] = a[i]%min_a
    if a_dict.get(a[i]) is None:
        a_dict[a[i]] = 1
        if a[i] != 0:
            ans = gcd(ans, a[i])
            if ans == 1:
                break

print(ans)



