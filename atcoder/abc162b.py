n = int(input())
sum_n = 0
for i in range(1, n):
    if i%3 != 0 and i%5 != 0:
        sum_n += i
print(sum_n)