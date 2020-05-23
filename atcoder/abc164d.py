s = input()
count = 0
if len(s) <= 4:
    print(0)
else:
    i = 0
    flag = 0
    flag_num = -1
    while i < len(s) - 4:
        j = i + 4
        digit_sum = sum(map(int, list(s[i:j]))) % 3
        mod = int(s[i:j]) % 673
        while j < len(s):
            now_sum = digit_sum + int(s[j]) % 3
            mod = (10*mod+int(s[j])) % 673
            if now_sum == 0 or now_sum == 3:
                if mod == 0:
                    # print(s[i:j+1], i, j, flag)
                    if i == flag_num:
                        count += 1 + flag
                        flag += 1
                    else:
                        count += 1
                        flag = 1
                    i = j
                    j = i + 3
                    flag_num = i+1
                    digit_sum = sum(map(int, list(s[i:i + 4]))) % 3
                    mod = int(s[i:i + 4]) % 673
            else:
                digit_sum = now_sum % 3
            j += 1
        i += 1
        if i > flag_num:
            flag = 0
    print(count)
