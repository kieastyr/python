import threading
import time

def func1():
    while True:
        print("私は工藤です")
        time.sleep(7/8)


def func2():
    while True:
        print("私はKPです")
        time.sleep(41/50)

if __name__ == "__main__":
    thread1 = threading.Thread(target=func1)
    thread2 = threading.Thread(target=func2)
    
    thread1.start()
    thread2.start()
