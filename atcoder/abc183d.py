import sys
def input():
    return sys.stdin.readline()[:-1]

n, w = map(int, input().split())
s_dict = {}
t_dict = {}
p_dict = {}

for i in range(n):
    s, t, p = map(int, input().split())
    if s_dict.get(s):
        s_dict[s].append(i)
    else:
        s_dict[s] = [i]
    if t_dict.get(t):
        t_dict[t].append(i)
    else:
        t_dict[t] = [i]
    p_dict[i] = p

s_tuple = sorted(s_dict.items())
t_tuple = sorted(t_dict.items())
ns = 0
nt = 0
i = s_tuple[ns][0]
sum = 0
num_s = len(s_dict)
num_t = len(t_dict)
while nt < num_t:
    if ns < num_s and i == s_tuple[ns][0]:
        for l in s_tuple[ns][1]:
            sum += p_dict[l]
        ns += 1
    if i == t_tuple[nt][0]:
        for l in t_tuple[nt][1]:
            sum -= p_dict[l]
        nt += 1
    if sum > w:
        print("No")
        exit()
    i += 1

print("Yes")