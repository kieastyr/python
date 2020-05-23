x = int(input())
year = 0
m = 100
while m < x:
    year += 1
    m = int(m*1.01)
print(year)
