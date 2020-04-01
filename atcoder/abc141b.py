out = 'Yes'
str = input()
for i,s in enumerate(str):
  if s == 'L' and i%2 == 0:
    out = 'No'
  elif s == 'R' and i%2 == 1:
    out = 'No'
print(out)