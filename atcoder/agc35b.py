# scanf的な（input()はstr型で入ってくるからintに変換してる）
n, m = map(int, input().split())

if m%2==1:
	print(-1)
else:
	# 二次元配列作ってる
	edge = [[] for i in range(n+1)]

	for i in range(1,m+1):
		# scanf的な（input()はstr型で入ってくるからintに変換してる）
		a, b = map(int, input().split())
		
		# edgeのa番目の配列にbを追加する
		edge[a].append(b)
		# edgeのb番目の配列にaを追加する
		edge[b].append(a)
	print(edge[1:])
	
	# 全部0の長さn+1の配列はこうするらしい
	flag = [0]*(n+2)
	out = []
	for i,connect in enumerate(edge, 1):
		if len(connect)%2 == 1:
			flag[i] = 1

	print(len(flag))
	for i,connect in enumerate(edge, 1):
		if flag[i] == 0:
			for j in connect:
				if flag[j] == 1:
					out.append([i, j])
					edge[i].pop(j)
					edge[j].pop(i)
				else:
					out.append([i, j])
			
	print(out)
    