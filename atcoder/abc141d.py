import math
n, m = map(int, input().split())
a = sorted(map(int, input().split()), reverse=True)
i = 1
while m > 0:
	if m>=i:
		m -= i
		a[0:i] = [num//2 for num in a[0:i]]
		while i>0 and a[i-1] == 0:
			del a[i-1]
			i -= 1
		if i == 0:
			break
		j = 0
		while i+j < n-1 and a[0]<a[i+j]:
			j += 1
		if j!=0:
			temp = a[i:i+j]
			a[j:i+j] = a[0:i]
			a[0:j] = temp
			i += 1
			
	else:
		a[0:m] = [num//2 for num in a[0:m]]
		m=0
if len(a)>0:
	print(sum(a))
else:
	print(0)