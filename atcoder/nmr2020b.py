t_in = input()
t_out = ""
for t in t_in:
    if t == '?':
        t_out += 'D'
    else:
        t_out += t
print(t_out)
