# t = int(input())
# for _ in range(t):
n, a, b, c, d = map(int, input().split())
x = n
max_cost = d*n
mods = [5, 3, 2]
costs = [c, b, a]
min_coin = d*n
mod2_cost = [a, a+d]
mod3_cost = [b, b+d, b+d]
mod5_cost = [c, c+d, c+2*d, c+2*d, c+d]


def search(x, cost):
    if x == 1:
        return cost + d
    elif x == 0 or x < 2*n:
        return 1e20
    mod2 = x % 2
    mod3 = x % 3
    mod5 = x % 5
    cost2 = mod2_cost[mod2]
    cost3 = mod3_cost[mod3]
    cost5 = mod5_cost[mod5]
    if 1.5*cost2 < cost3 and 2.5*cost2 < cost5:
        x = min(search(x//2, cost + a + d*mod2), search(x//2+1, cost + a + d*(2-mod2)))
    elif cost3 < 5/3*cost5:
        x = min(search(x//3, cost + b + d*mod3), search(x//3+1, cost + b + (3-mod3)))
    else:
        x = min(search(x//5, cost + c + d*mod5), search(x//5+1, cost + c + (5-mod5)))
    return x


print(search(x, 0))
