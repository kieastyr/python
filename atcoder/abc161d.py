k = int(input())
if k < 10:
    print(k)
else:
    k -= 9
    run= {}
    run[1] = {i: 1 for i in range(0, 10)}
    now_dig = 1
    flag = 0
    ans = 0
    while flag == 0:
        now_dig += 1
        run[now_dig] = {}
        for num in range(0, 10):
            if num == 0:
                run[now_dig][num] = run[now_dig-1][num] + run[now_dig-1][num+1]
            elif num == 9:
                run[now_dig][num] = run[now_dig-1][num-1] + run[now_dig-1][num]
            else:
                run[now_dig][num] = run[now_dig-1][num-1] + run[now_dig-1][num] + run[now_dig-1][num+1]
            if num != 0 and k - run[now_dig][num] > 0:
                k -= run[now_dig][num]
            elif num != 0:
                flag = 1
                # print(k, now_dig, num)
                ans += num*pow(10, now_dig-1)
                while now_dig > 1:
                    now_dig -= 1
                    if num == 0:
                        now_num = 0
                        end = 1
                    elif num == 9:
                        now_num = 8
                        end = 9
                    else:
                        now_num = num - 1
                        end = num + 1
                    while k - run[now_dig][now_num] > 0 and now_num <= end:
                        k -= run[now_dig][now_num]
                        now_num += 1
                    ans += now_num*pow(10, now_dig-1)
                    num = now_num
                break
        print(now_dig, run[now_dig])

    print(ans)
