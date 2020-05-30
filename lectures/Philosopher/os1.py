import time
import threading
import random
fork = [0,0,0,0,0]

def waiter(i):
    if ((fork[i%5] == 0 and fork[(i+1)%5] ==0) or
    (fork[i%5] == i and fork[(i+1)%5] ==0) ):
        return 1
    else:
        return 0


class tetsu(threading.Thread):
    def __init__(self,i):
        super(tetsu, self).__init__()
        self.i = i

    def run(self):
        while True:
            time.sleep(random.uniform(1,5))
            i = self.i
            if fork[i%5] == 0 and waiter(i)==1:
                fork[i%5]=i
            elif fork[(i+1)%5] == 0 and waiter(i)==1:
                fork[(i+1)%5]=i
            elif fork[i%5] ==fork[(i+1)%5]:
                time.sleep(3)
                print("哲学者%dが食べました"%i)
                fork[(i+1)%5]=0
                fork[i%5] =0
            print(fork)



if __name__ == '__main__':
    te1 = tetsu(1);
    te2 = tetsu(2);
    te3 = tetsu(3);
    te4 = tetsu(4);
    te5 = tetsu(5);
    te1.start()
    te2.start()
    te3.start()
    te4.start()
    te5.start()
