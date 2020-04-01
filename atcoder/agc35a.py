n = input()
a = list(map(int, input().split()))
ring = [a[0]]
flag = 0
num = n-1
for i in range(n-1):
	while(not(ring[i]^a[j] in a[0:j] or ring[i]^a[j] in a[j+1:n]) and j<num):
		j += 1
	if j>=num:
		flag = 1
	else:
		