import math
 
s = int(input())
rs = int(math.sqrt(2*s))
rem_s = rs**2-s
x1=0
if rem_s==0:
	print(0,0,rs,0,0,rs)
else:
	div = 1
	if rem_s%2 != 0:
		for i in range(3,int(4*1e+4)+1,2):
			if rem_s%i==0 and rem_s//i<=1e+9:
				div = i
				break
	else:
		div=2
	if rem_s <0:
		x1 = -rem_s//div
	print(x1,0,rs+x1,div,rem_s//div+x1,rs)