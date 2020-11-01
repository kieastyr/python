n = int(input())
x_list = map(int, input().split())

man_sum = 0
euc_sum = 0
che_max = 0

for x in x_list:
    man_sum += abs(x)
    euc_sum += x**2
    if che_max < abs(x):
        che_max = abs(x)

print(man_sum)
print(euc_sum**(1/2))
print(che_max)
