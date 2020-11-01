n, m = map(int, input().split())
h_list = list(map(int, input().split()))
w_list = list(map(int, input().split()))
h_list.sort()
w_list.sort()

l_dis = [0]
r_dis = [0]

for i in range(n//2):
    l_dis.append(l_dis[i]+h_list[2*i+1]-h_list[2*i])
    r_dis.append(r_dis[i]+h_list[-(2*i+1)]-h_list[-2*(i+1)])

print(l_dis)
print(r_dis)

m_dis = []
hi = 0
wi = 0
while wi < m:
    while hi < n and h_list[hi] < w_list[wi]:
        hi += 1
    # print(l_dis[hi//2], h_list[hi], w_list[wi], r_dis[(n-hi)//2])
    if hi == n:
        m_dis.append(l_dis[-1]+w_list[wi]-h_list[-1])
    if hi %2 == 0:
        m_dis.append(l_dis[hi//2]+h_list[hi]-w_list[wi]+r_dis[(n-hi)//2])
    else:
        m_dis.append(l_dis[hi//2]+w_list[wi]-h_list[hi-1]+r_dis[(n-hi)//2])
    
    wi += 1

print(m_dis)
print(min(m_dis))