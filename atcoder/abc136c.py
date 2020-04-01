n = int(input())
h = list(map(int, input().split()))
flag = 0
result = 1
for i in range(n-1):
	if h[i]==h[i+1]+1 and flag==0:
		flag=1
	elif h[i]==h[i+1] and flag==1:
		continue
	elif h[i]<=h[i+1]:
		flag=0
	else:
		result = 0
if result:
	print("Yes")
else:
	print("No")