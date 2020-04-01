s = input()
result = [0]*len(s)
r_end = 0
l_head = 1
i = 0
while i <len(s):
	r_count = 0
	l_count = 0
	while i<len(s) and s[i]=='R':
		i += 1
		r_count += 1
	r_end = i-1
	l_head = i
	while i<len(s) and s[i]=='L':
		i += 1
		l_count += 1
	result[r_end] += int(round(r_count/2+0.1))
	result[l_head] += r_count//2
	result[r_end] += l_count//2
	result[l_head] += int(round(l_count/2+0.1))
for i in range(len(s)):
	print(result[i],end=' ')