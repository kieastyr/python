x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p_eat = sorted(p, reverse=True)[:x]
q_eat = sorted(q, reverse=True)[:y]
r_eat = sorted(r, reverse=True)

def nap(x_rem, y_rem, x_i, y_i, r_i, sum_yammy):
    if x_rem == 0 and y_rem == 0:
        return sum_yammy
    elif x_rem == 0:
        if y_i < y:
            nap1 = nap(x_rem, y_rem-1, x_i, y_i+1, r_i, sum_yammy+q_eat[y_i])
        else:
            nap1 = 0
        if r_i < c:
            nap2 = nap(x_rem, y_rem-1, x_i, y_i, r_i+1, sum_yammy+r_eat[r_i])
        else:
            nap2 = 0
        return max([nap1, nap2])
    elif y_rem == 0:
        if x_i < x:
            nap1 = nap(x_rem-1, y_rem, x_i+1, y_i, r_i, sum_yammy+p_eat[x_i])
        else:
            nap1 = 0
        if r_i < c:
            nap2 = nap(x_rem-1, y_rem, x_i, y_i, r_i+1, sum_yammy+r_eat[r_i])
        else:
            nap2 = 0
        return max([nap1, nap2])
    else:
        if x_i < x:
            nap1 = nap(x_rem-1, y_rem, x_i+1, y_i, r_i, sum_yammy+p_eat[x_i])
        else:
            nap1 = 0
        if y_i < y:
            nap2 = nap(x_rem, y_rem-1, x_i, y_i+1, r_i, sum_yammy+q_eat[y_i])
        else:
            nap2 = 0
        if r_i < c:
            nap3 = nap(x_rem-1, y_rem, x_i, y_i, r_i+1, sum_yammy+r_eat[r_i])
            nap4 = nap(x_rem, y_rem-1, x_i, y_i, r_i+1, sum_yammy+r_eat[r_i])
        else:
            nap3, nap4 = 0, 0
        return max([nap1, nap2, nap3, nap4])

print(nap(x, y, 0, 0, 0, 0))
