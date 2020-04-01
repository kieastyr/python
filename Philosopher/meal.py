'''
食事をする哲学者の問題
モニタによる解法
'''
import threading as th
import time
import random as rn
import sys

printPhilo = [" O ", " O|", "|O ", "|O|", " X "]    #順に何もなし，右の箸あり，左あり，両方あり，飢餓
printHashi = ["|", " "] #あり/なし
philoName = ["Socrates", "Plato", "Aristotles", "Pythagoras", "Thales"]

phArray = []                
hashi = [0, 0, 0, 0, 0]    #値はprintHashiのkeyに対応．位置はphilo_iの両端にhashi[i],hashi[(i+1)%5]
mode = int(sys.argv[1])        #0:デッドロック起きるモード  1:デッドロック起きないモード
#mode = 1
print("mode:"+str(mode))

class philo(th.Thread):
    phase = 0       #0:思慮状態， 1:食事状態
    phStatus = 0    #状態．printPhiloのキー
    hungry = 0         #飢餓の基準
    def __init__(self, i):
        super(philo, self).__init__()
        self.i = i                  #人の番号
        self.name = philoName[i]    #人の名前
    def run(self):
        i = self.i
        while True:   
            if self.phase == 0:
                time.sleep(rn.uniform(3,5)) #3~5秒間の思慮
                self.phase = 1				#食事モードへ
            elif self.phase == 1:   #食事に入る
                time.sleep(2)
                if self.hungry>=20:
                    self.phStatus = 4       #状態4:飢餓
                elif self.phStatus<=2:
                    self.hungry += 1
                
                result = useHashi(i)
                if result == "getRight":
                    self.phStatus += 1      #0なら1,2なら3に
                    hashi[(i+1)%5] = 1
                elif result == "getLeft":
                    self.phStatus += 2      #0なら2,1なら3に
                    hashi[i] = 1
                elif result == "putRight":
                    print(self.name+"さんが右の箸を置きました")
                    self.phStatus -= 1      #1なら0,3なら2に
                    hashi[(i+1)%5] = 0
                elif result == "putLeft":
                    print(self.name+"さんが左の箸を置きました")
                    self.phStatus -= 2      #2なら0,3なら1に
                    hashi[i] = 0                
                
                if self.phStatus==3: #状態3:箸を2本持っている
                    eat(i)
                    self.phStatus = 0
                    self.phase = 0        #思慮に入る
                
def useHashi(i):    #箸を取るか置くかの判断
    if mode==0:     #デッドロック起きるモード    
        if hashi[i]==0:
            return "getLeft"
        elif hashi[(i+1)%5] == 0:
            return "getRight"
    elif mode==1:   #デッドロック起きないモード
        pa = phArray
        if hashi[i]==0 and pa[i].hungry >= pa[(i-1)%5].hungry:
            #競合相手よりお腹が空いているなら取る
            return "getLeft"
        elif hashi[(i+1)%5] == 0 and pa[i].hungry >= pa[(i+1)%5].hungry:
            #競合相手よりお腹が空いているなら取る
            return "getRight"
        elif pa[i].phStatus==2 and (pa[(i+1)%5].phStatus==2 or pa[(i+1)%5].phStatus==3):
            #競合相手にもう1つを取られているなら置く
            return "putLeft"
        elif pa[i].phStatus==1 and (pa[(i-1)%5].phStatus==1 or pa[(i-1)%5].phStatus==3):
            #競合相手にもう1つを取られているなら置く
            return "putRight"

def eat(i):
    time.sleep(3)
    hashi[i] = 0
    hashi[(i+1)%5] = 0
    print(phArray[i].name+"さんが食べ終わりました．")
    phArray[i].hungry = 0

def show():
    while True:
        time.sleep(1)
        for i in range(5):
            print(" "+printPhilo[phArray[i].phStatus], end=" ")
        print(" ")
    
        for i in range(6):
            if i<5:
                print(printHashi[hashi[i]]+"{0:2d} ".format(phArray[i].hungry), end=" ")
            else:
                print(printHashi[hashi[0]])
        print(" ")

def inputMode():	#実行中にモードを変えたくなった時用
    while True:
        global mode
        mode = int(input())
        print("MODE CHANGED!:"+str(mode))

if __name__ == "__main__":
    for i in range(5):
        phArray.append(philo(i))
        phArray[i].start()

    viewStatus = th.Thread(target=show)
    modeChange = th.Thread(target=inputMode)
    viewStatus.start()
    modeChange.start()
