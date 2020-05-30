'''
Created on 2018/01/02

@author: Kai_Kudo
'''
import tkinter as tk
import time
import random

def getFileName():
    flag = 0
    fileName = {
        0 : "N_B",
        1 : "N_I",
        2 : "N_S",
        10 : "V_B",
        11 : "V_I",
        12 : "V_S",
        20 : "Adj_B",
        21 : "Adj_I",
        }
    choice1 = {0:'名詞',1:'動詞',2:'形容詞'}
    choice2 = {0:'初級',1:'中級',2:'上級'}
    radio_value = tk.IntVar()
    radio_value.set()
    for i in choice1:
        tk.Radiobutton(base, text=choice1[i], variable=radio_value, value=i).pack()
    def next():
       
    tk.Button(base, text='選択', command=next).pack() 
    
       
    return 'question_'+fileName[num]+'.txt'

base = tk.Tk()
f = open(getFileName(), 'r')
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

