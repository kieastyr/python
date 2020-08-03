n = int(input())
a_list = list(map(int, input().split()))
money = 1000
stock = 0
for i in range(n-1):
    if a_list[i+1] < a_list[i]:
        money += stock*a_list[i]
        stock = 0
    elif a_list[i+1] > a_list[i]:
        new_stock = money//a_list[i]
        money -= new_stock*a_list[i]
        stock += new_stock

print(money+stock*a_list[n-1])
