n, k = map(int, input().split())
a = list(map(int, input().split()))
count = [0]*200001
out = []
'''
for i in a:
	count[i] += 1
count = list(map(lambda x: x * k, count))
print(count[:len(a)])
'''
flag = 0
for num,ai in enumerate(reversed(a)):
	if count[ai]==0:
		count[ai] += 1
	else if flag==0:
		out_temp = a[num+1:]
		flag += 1
	else if flag==1:
		out_temp2 = out_temp[out_temp.index(ai)+1:]
		