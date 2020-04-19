'''
Created on 2019/07/08

@author: B4
'''

mod = 1e9+7

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    sum_a = 0
    i = 0
    for l in range(n):
        while sum_a<k and i<n:
            sum_a += a[i]
            i += 1
        if sum_a>=k:
            count += n-i+1
            sum_a -= a[l]
    print(count)
        