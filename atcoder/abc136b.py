n = int(input())
sum = 0
if n//10!=0:
  sum+=9
  if n//1000!=0:
    sum+=900
    if n//100000!=0:
      sum+=90000
    elif n//10000!=0:
      sum+=n-9999
  elif n//100!=0:
    sum+=n-99
else:
  sum+=n
print(sum)