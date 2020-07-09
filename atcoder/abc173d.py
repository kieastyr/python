n = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)
# print(a_list)
ans = a_list[0]
if n % 2 == 1:
    ans += 2 * sum(a_list[1:(n-1)//2]) + a_list[(n-1)//2]
else:
    ans += 2 * sum(a_list[1:n//2])
print(ans)
