x, y, a, b = map(int, input().split())

ans = 0

while x < y:
    if x*a >= y and x + b >= y:
        break
    elif x*(a-1) < b:
        x *= a
        ans += 1
    else:
        ans += (y-x-1)//b
        x += b*((y-x-1)//b)

print(ans)
