import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 

k = int(input())
s = input()
t = input()
card = {i: k for i in range(1, 10)}
s_card = {i: 0 for i in range(1, 10)}
t_card = {i: 0 for i in range(1, 10)}

for i, j in zip(list(s)[:4], list(t)[:4]):
    s_card[int(i)] += 1
    card[int(i)] -= 1
    t_card[int(j)] += 1
    card[int(j)] -= 1

s_win = 0
for i in range(1, 10):
    if card[i] > 0:
        s_card[i] += 1
        c_i = card[i]
        for j in range(1, 10):
            if card[j] > 0:
                t_card[j] += 1
                c_j = card[j]
                s_score = 0
                t_score = 0
                for l in range(1, 10):
                    s_score += l*10**s_card[l]
                    t_score += l*10**t_card[l]
                if s_score > t_score:
                    if i != j:
                        s_win += c_i*c_j
                        # print(i, j, c_i*c_j)
                    else:
                        s_win += c_i*(c_j-1)
                        # print(i, j, c_i*(c_j-1))
                t_card[j] -= 1
        s_card[i] -= 1

print(s_win/((9*k-8)*(9*k-9)))
