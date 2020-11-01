n_list = {}
a = 1
x = 0
while 3**a <= 1e18:
    b = 1
    while True:
        x = 3**a + 5 **b
        if x > 1e18:
            break
        else:
            n_list[x] = [a, b]
            b += 1
    a += 1

n = int(input())
if n_list.get(n):
    print(f"{n_list[n][0]} {n_list[n][1]}")
else:
    print(-1)