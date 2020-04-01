def cd(num, max):
	cd_list = []
	for i in reversed(range(1,max+1)):
		if num%i==0:
			cd_list.append(i)
	return cd_list

n, k = map(int, input().split())
a = list(map(int, input().split()))
cd_list = cd(sum(a),sum(a)//n)
for num in cd_list:
	rem=0
	for i in a:
		rem += abs(i-num*round(i/num))
	if rem//2<=k:
		print(num)
		break