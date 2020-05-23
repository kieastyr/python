def f(a, b):
    return a**4 + a**3 * b + a**2 * b**2 + a * b**3 + b**4


x = int(input())
pair = [(1, x)]
i = 2
while i*i <= x:
    if x % i == 0:
        pair.append((i, x//i))
    i += 1

for i, j in pair:
    # print(f"pair:{i} {j}")
    a = 0
    b = -i
    while b <= 0 or f(a, b) <= j:
        # print(f(a, b))
        a += 1
        b += 1
        if f(a, b) == j:
            print(f"{a} {b}")
            exit(0)
