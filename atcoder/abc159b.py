s = input()
n = len(s)
n2 = (n-1)//2
flag = 1
for i in range(n2):
  if not((s[i] == s[n-i-1]) and (s[i] == s[n2-1-i]) and (s[i] == s[n2+i+1])):
    flag = 0
if flag == 1:
  print("Yes")
else:
  print("No")