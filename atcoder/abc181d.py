s_in = input()
if int(s_in)%8 == 0:
    print("Yes")
elif len(s_in) == 2 and int(s_in[::-1]) % 8 == 0:
    print("Yes")
else:
    s_dict = {i: 0 for i in range(10)}
    for s in s_in:
        s_dict[int(s)] += 1

    eighter = [8*i for i in range(125)]
    eighter_dict = {i: {} for i in range(10)}
    for e in eighter:
        if eighter_dict[e//100].get(e%100//10):
            eighter_dict[e//100][e%100//10].append(e%10)
        else:
            eighter_dict[e//100][e%100//10] = [e%10]

    ans = "No"
    for i in range(10):
        if s_dict[i] >= 1:
            s_dict[i] -= 1
            for j in eighter_dict[i].keys():
                if s_dict[j] >= 1:
                    s_dict[j] -= 1
                    for k in eighter_dict[i][j]:
                        if s_dict[k] >= 1:
                            ans = "Yes"
                            break
                    
                    if ans == "Yes":
                        break
                    s_dict[j] += 1
                
            if ans == "Yes":
                break
            s_dict[i] += 1
        
    print(ans)
