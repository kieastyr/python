import time
import urllib.request
import random
import numpy as np
import copy

#一番良いものと異なっていると加点
def diff(str1, str2):
	score = 0
	for i in range(50):
		if(str1[i]!=str2[i]):
			score += 10
	return score

def cross_gene(score):
	gene_num = random.randrange(sum(score))
	i=-1
	while(gene_num>0):
		gene_num -= score[i]
		i += 1;
	return i

def query(url):
	req = urllib.request.Request(url)
	with urllib.request.urlopen(req) as res:
		return res.read()

token = "NAKBo6doM8qtbAvQp9bvBJ9Uk4wNtKXL"
letter = ['A', 'B', 'C', 'D']
gene_num = 10
generation_num = 5
mutetion = 0.02
str_gene = []
score = [0]*gene_num

'''
#初期値をランダムに設定
for gene in range(gene_num):
	temp = ""
	for length in range(50):
		temp += random.choice(letter)
	str_gene.append(temp)
	url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, temp)
	score[gene] = int(query(url).decode("UTF-8"))
	print(temp, score[gene])
	time.sleep(1)
'''

#テキストからgeneとその個数を取得
with open("gene1.txt", mode='r') as f:
	gene = 0
	for text in f:
		str_gene.append(text)
		url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, text)
		score[gene] = int(query(url).decode("UTF-8"))
		time.sleep(1)
		print(text, score[gene])
		gene += 1

#進化
for generation in range(generation_num):
	print(f"No.{generation}")
	new_gene = copy.deepcopy(str_gene)
	new_score = copy.deepcopy(score)
	for gene in range(gene_num):
		#交叉
		slice_point1 = random.randrange(1,25)
		slice_point2 = random.randrange(26,49)
		new_gene_temp = str_gene[cross_gene(score)][:slice_point1]+str_gene[cross_gene(score)][slice_point1:slice_point2]+str_gene[cross_gene(score)][slice_point2:]
		
		#突然変異
		for length in range(1,49):
			if random.random() < mutetion:
				new_gene_temp = new_gene_temp[:length-1]+random.choice(letter)+new_gene_temp[length:]
		
		#評価
		url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, new_gene_temp)
		score_temp = int(query(url).decode("UTF-8"))+diff(new_gene_temp,new_gene[0])
		print(new_gene_temp, score_temp)
		time.sleep(1)
		new_gene.append(new_gene_temp)
		new_score.append(score_temp)
		
	score_culc = np.array(new_score)
	max_score = np.max(score_culc)
	max_str = new_gene[np.argmax(score_culc)]
	print(f"max_point:{max_score} {max_str}")
	
	#既存と新規のうちscoreが高いものgene_num個を選別
	for num in range(gene_num):
		largest = np.array(new_score).argmax()
		str_gene[num] = new_gene[largest]
		new_gene.pop(largest)
		score[num] = new_score[largest]
		new_score.pop(largest)

#結果を保存		
with open("gene1.txt", mode='w') as f:
	f.writelines(str_gene)

'''
#
for length in range(50):
	print(f"length={length}")
	max_point = 0
	for i, add_letter in enumerate(letter):
		new_str[i] = str+add_letter
		url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, new_str[i])
		result = int(query(url).decode("UTF-8"))
		if result>max_point:
			max_point = result
			temp_max_str = new_str[i]
		print(new_str[i], result, temp_max_str, max_point)
		time.sleep(1)
	str = temp_max_str
'''