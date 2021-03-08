n = int(input())
a_list = list(map(int, input().split()))

counter = {i:0 for i in range(2, max(a_list)+1)}
for k in counter.keys():
    for a in a_list:
        if a%k == 0:
            counter[k] += 1
        
print(max(counter, key=counter.get))
