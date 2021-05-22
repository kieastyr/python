import sys
import math

def input():
    return sys.stdin.readline()[:-1]

mod = int(10**9+7)

n = int(input())
a = list(map(int, input().split()))

a_left = [0 for _ in range(n)]
a_center = [0 for _ in range(n)]
a_right = [0 for _ in range(n)]

area_end = {}
ans = 0

for i in range(n):
    if i > 0:
        a_left[i] = a[i]-a[i-1]
    if i < n-1:
        a_right[i] = a[i]-a[i+1]
    if i > 0 and i < n-1:
        a_center[i] = a[i]-a[i-1]-a[i+1]
    
    if i > 0 and a_left[i] == 0:
        if area_end.get(i-2):
            area_end[i] = area_end[i-2]+1
        else:
            area_end[i] = 1
        ans += area_end[i]
        # print('l', i-1, i)
    # elif i < n-1 and a_right[i] == 0:
    #     if area_end.get(i-1):
    #         area_end[i+1] = area_end[i-1]+1
    #     else:
    #         area_end[i+1] = 1
    #     ans += area_end[i+1]
    #     print('r', i, i+1)
    elif i > 0 and i < n-1 and a_center[i] == 0:
        if area_end.get(i-2):
            area_end[i+1] = area_end[i-2]+1
        else:
            area_end[i+1] = 1
        ans += area_end[i+1]
        # print('c', i-1, i+1)
    else:
        if i >= 3:
            if i < n-1 and a_center[i] == a_right[i-3]:
                if area_end.get(i-4):
                    area_end[i+1] = area_end[i-4]+1
                else:
                    area_end[i+1] = 1
                ans += area_end[i+1]
                # print('rc', i-3, i+1)
            elif a_left[i] == a_right[i-3]:
                if area_end.get(i-4):
                    area_end[i] = area_end[i-4]+1
                else:
                    area_end[i] = 1
                ans += area_end[i]
                # print('rl', i-3, i)
        if i >= 4:
            if i < n-1 and a_center[i] == a_center[i-3]:
                if area_end.get(i-5):
                    area_end[i+1] = area_end[i-5]+1
                else:
                    area_end[i+1] = 1
                ans += area_end[i+1]
                # print('cc', i-4, i+1)
            # elif a_left[i] == a_center[i-3]:
            #     if area_end.get(i-5):
            #         area_end[i] = area_end[i-5]+1
            #     else:
            #         area_end[i] = 1
            #     ans += area_end[i]
            #     print('cl', i-4, i)

print(ans)
