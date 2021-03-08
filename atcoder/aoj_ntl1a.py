n = int(input())
i = 2
ans = []
while n%2 == 0:
    n //= i
    ans.append(i)

i = 3
while n != 1:
    while n%i == 0:
        n //= i
        ans.append(i)
    i += 2

print(f"{n}: ")
