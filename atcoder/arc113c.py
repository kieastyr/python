import sys
import math
def input():
    return sys.stdin.readline()[:-1]

mod = 998244353 
dic = {}
s_list = list(input())[::-1]
# print(s_list)
l = len(s_list)
i = 0
ans = 0
while i < l-2:
    if s_list[i+1] == s_list[i+2] and s_list[i] != s_list[i+1]:
        ans += i+1 - dic.get(s_list[i+1], 0)
        del dic
        dic = {s_list[i+1]: i+1}
    else:
        if dic.get(s_list[i]):
            dic[s_list[i]] += 1
        else:
            dic[s_list[i]] = 1
    i += 1
    
print(ans)
