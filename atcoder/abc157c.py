def main():
    n, m = map(int, input().split())
    s_dict = {}
    sum = 0
    for _ in range(m):
        s, c = map(int, input().split())
        if s in s_dict and s_dict[s] != c or n!=1 and s==1 and c==0:
            sum = -1
            break
        else:
            s_dict[s] = c
    
    if sum != -1:
        for i in range(1, n+1):
            if i in s_dict:
                sum += s_dict[i]*pow(10, n-i)
            elif i == 1 and n != 1:
                sum += pow(10, n-1)
    print(sum)

if __name__=='__main__':
    # import time
    # start = time.time()
    main()
    # print(f"{time.time()-start}[s]")
