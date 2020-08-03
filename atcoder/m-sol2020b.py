a, b, c = map(int, input().split())
k = int(input())
flag = 0


def map(now_a, now_b, now_c, now_k):
    if now_a < now_b and now_b < now_c:
        return 1
    elif now_k == 0:
        return 0
    else:
        r1 = map(now_a*2, now_b, now_c, now_k-1)
        r2 = map(now_a, now_b*2, now_c, now_k-1)
        r3 = map(now_a, now_b, now_c*2, now_k-1)
        if r1+r2+r3 == 0:
            return 0
        else:
            return 1


if map(a, b, c, k) == 0:
    print("No")
else:
    print("Yes")

