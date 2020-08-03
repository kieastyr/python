import math
n, k = map(int, input().split())
a_list = sorted(list(map(int, input().split())))
pow_list = []
min_a = a_list[0]
for i in range(1,n):
    while a_list[i] > 2*min_a:
        pow_list.append(i-1)
        min_a *= 2


pow_list.append(n-1)
k_num = 0
for i, num in enumerate(pow_list):
    k_num += i*num

if k < k_num:
    pow_len = len(pow_list)
    i = pow_len-2
    longest_i = n-1
    longest = a_list[longest_i]
    print(a_list)
    print(pow_list)
    while k >= pow_list[pow_len-1] - pow_list[i]:
        k -= pow_list[pow_len-1] - pow_list[i]
        longest /= 2
        if a_list[pow_list[i]] > longest:
            longest_i = pow_list[i]
            longest = a_list[longest_i]
        i -= 1
    new_list = sorted(a_list[pow_list[i]+1:])
    print(new_list)
    tei_i = i
    pow_i = i
    for i in range(len(new_list)):
        if i == pow_list[pow_i]+1:
            pow_i += 1
        new_list[i] /= 2**(pow_i - tei_i)
    print(new_list)
    longest = new_list[-(k+1)]
else:
    k -= k_num
    pow_i = 0
    for i in range(pow_list[0]+1, n):
        if i == pow_list[pow_i]+1:
            pow_i += 1
        a_list[i] /= 2**pow_i
    
    a_list.sort()
    
    r = k // n
    m = k % n
    longest = a_list[n-1-m] / (2**r)

print(math.ceil(longest))
