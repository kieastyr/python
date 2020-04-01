a, b, c = map(int, input().split())
eq = (c-a-b)**2-4*a*b
if eq > 0:
    print("Yes")
else:
    print("No")