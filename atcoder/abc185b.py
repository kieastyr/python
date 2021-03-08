import sys
def input():
    return sys.stdin.readline()[:-1]


rps_dict = {"R": 11, "P": 7, "S": 5}
rps_invdict = {11: "R", 7: "P", 5: "S"}
n, m, t = map(int, input().split())

now_b = n
now_t = 0
for i in range(m):
    a, b = map(int, input().split())
    now_b -= (a-now_t)
    if now_b <= 0:
        print("No")
        exit()
    now_b = min(n, now_b+(b-a))
    now_t = b

if now_b > t-now_t:
    print("Yes")
else:
    print("No")
