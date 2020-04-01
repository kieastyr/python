'''
Created on 2018/01/02

@author: Kai_Kudo
'''
import time
import random

def setQuestion():
    flag = 0
    fileName = {
        11 : "N_B",
        12 : "N_I",
        13 : "N_S",
        21 : "V_B",
        22 : "V_I",
        23 : "V_S",
        31 : "Adj_B",
        32 : "Adj_I",
        }
    while flag==0:
        print("選択>\n1:名詞\n2:動詞\n3:形容詞")
        num = int(input())
        if(1<=num<=3):
            flag += 1
            while True:
                print("選択>\n1:初級\n2:中級\n3:上級")
                n = int(input())
                if((10*num+n) in fileName):
                    num = 10*num + n
                    return 'question_'+fileName[num]+'.txt'

f = open(setQuestion(), 'r')
line = f.readline()
i = 0
q = {}
while line:
    i += 1
    #print(line, end='')
    q[i] = line
    line = f.readline()
f.close()

random.seed()
t0 = time.time()
t1 = 0
t_limit = 60
score = 0

while (t_limit-t1>=0):
    print("残り時間:%0.2f\t得点:%d"%(t_limit-t1, score))
    r = random.randrange(len(q))
    print(q[r], end='')
    ans = input()
    i = 0
    point = [0, 0]
    while (('a'<=q[r][i]<='z')or('A'<=q[r][i]<='Z')
           or(q[r][i]==' ')or(q[r][i]=='-')):
        if(i<len(ans) and ans[i]==q[r][i]):
            print(' ', end='')
            point[0] += 1
        else:
            print('^', end='')
            point[1] += 1
        i += 1    
    print("")    
    if(point[1]==0):
        print('correct!!')
    else:
        t0 -= point[1]
    print("")    
    score += point[0]
    t1 = time.time()-t0
    
print("時間切れ\n得点:"+str(score))

