n, k, q = map(int, input().split())
a = [0]*q
point = [k-q]*(n+1)
for i in range(q):
	point[int(input())] += 1
for i in range(1,n+1):
	if point[i] <= 0:
		print('No')
	else:
		print('Yes')