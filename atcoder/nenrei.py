import random

itr = 1000000
result = []

for i in range(itr):
    count = 0
    year = 0
    while year != 100:
        if random.random() < 0.5:
            year = year%10*10 + year//10
        year += 1
        count += 1

    # print(count)
    result.append(count)

print(sum(result)/itr)