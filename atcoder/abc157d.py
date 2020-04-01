def main():
    n, m, k = map(int, input().split())
    friends = [[0 for _ in range(n+1)] for _ in range(n+1)]
    block = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        friends[a][b] = 1
        friends[b][a] = 1
    for _ in range(k):
        a, b = map(int, input().split())
        block[a][b] = 1
        block[b][a] = 1
    # print(friends[1:], block[1:])

    cand_friends = [[0 for _ in range(n+1)] for _ in range(n+1)]
    def search_cand(now_node, i):
        for next_node, num in enumerate(friends[now_node]):
            if num == 1 and cand_friends[i][next_node] == 0:
                cand_friends[i][next_node] = 1
                search_cand(next_node, i)

    for i in range(1, n+1):
        now_node = i
        search_cand(now_node, i)
        cand_friends[i][i] = 0
        cand_num = sum(cand_friends[i]) - sum(friends[i])
        for b, num in enumerate(block[i]):
            if num==1 and cand_friends[i][b]==1:
                cand_num -= 1
        print(cand_num, end=' ')
    print("")
    # print(cand_friends[1:])

if __name__=='__main__':
    # import time
    # start = time.time()
    main()
    # print(f"{time.time()-start}[s]")
