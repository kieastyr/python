n = list(map(int, list(input())))
n_mod = list(map(lambda x: x%3, n))
# print(n, n_mod)

m = sum(n)%3
if m == 0:
    print(0)
elif m == 1:
    if len(n) >= 2 and n_mod.count(1) >= 1:
        print(1)
    elif len(n) >= 3 and n_mod.count(2) >= 2:
        print(2)
    else:
        print(-1)
elif m == 2:
    if len(n) >= 2 and n_mod.count(2) >= 1:
        print(1)
    elif len(n) >= 3 and n_mod.count(1) >= 2:
        print(2)
    else:
        print(-1)


