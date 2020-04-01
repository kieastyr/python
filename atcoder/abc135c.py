n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
rem = list(b)
sum = 0
rem[0] = b[0]-a[0] if a[0]<b[0] else 0
sum += b[0]-rem[0]
for i in range(1,n):
	if a[i]-rem[i-1]<0:
		sum += a[i]
	else:
		rem[i] = b[i]-(a[i]-rem[i-1]) if a[i]-rem[i-1]<b[i] else 0
		sum += rem[i-1]+b[i]-rem[i]
sum += rem[n-1] if a[n]>rem[n-1] else a[n]
print(sum)