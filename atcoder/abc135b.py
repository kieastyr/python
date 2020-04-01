# scanf的な（input()はstr型で入ってくるからintに変換してる）
n = int(input())
# 空白で区切られた数列はinputしたのをsplit()することで配列にできる
p = list(map(int, input().split()))
# コピー作るときにはq = pだとよくないらしい
q = p.copy()
# これだけでソートしてくれるのは便利
q.sort()

count = 0
# for文のこの書き方はおまじないだと思って
for i in range(n):
	if p[i]!=q[i]:
		count += 1
# andとかorはそのまま
if count==0 or count==2:
	print("YES")
# ちなみにelse ifってやりたい時はelifなんだけどこれはあんまり好きじゃない
else:
	print("NO")