import time
import threading



Fork = [0,0,0,0,0]
counter = [0,0,0,0,0]

def Waiter(n):
    global counter
    counter[n-1] = 0
    for i in range(len(Fork)):
        if Fork[i] == 0:
            counter[n-1] += 1
    print(i)


def Ph1():
    while True:

        if Fork[0] == 1 and Fork[1] == 1:
                time.sleep(1)
                print('Ph1が食べ終わりました')
                Fork[0] = 0
                Fork[1] = 0
                print('Ph1がフォークを机に置きました')
                print(Fork)

        elif Fork[0] == 1 and Fork[1] == 0:
                Fork[1] = 1
                print('Ph1が食事を始めました')
                print(Fork)
        elif Fork[0] == 0 and Fork[1] == 1:
                Fork[0] = 1
                print('Ph1が食事を始めました')
                print(Fork)
        elif Fork[0] == 0:
                Waiter(1)
                if counter[0] != 1:
                        Fork[0] = 1
                        print('Ph1が右手にフォークを持ちました')
                print(Fork)
        elif Fork[1] == 0:
                Waiter(1)
                if counter[0] != 1:
                        Fork[1] = 1
                        print('Ph1が左手にフォークを持ちました')
                print(Fork)


def Ph2():
    while True:

        if Fork[1] == 2 and Fork[2] == 2:
                time.sleep(1)
                print('Ph2が食べ終わりました')
                Fork[1] = 0
                Fork[2] = 0
                print('Ph2がフォークを机に置きました')
                print(Fork)
        elif Fork[1] == 2 and Fork[2] == 0:
                Fork[2] = 2
                print('Ph2が食事を始めました')
                print(Fork)
        elif Fork[1] == 0 and Fork[2] == 2:
                Fork[1] = 2
                print('Ph2が食事を始めました')
                print(Fork)
        elif Fork[1] == 0:
                Waiter(2)
                if counter[1] != 1:
                         Fork[1] = 2
                         print('Ph2が右手にフォークを持ちました')
                print(Fork)
        elif Fork[2] == 0:
                Waiter(2)
                if counter[1] != 1:
                        Fork[2] = 2
                        print('Ph2が左手にフォークを持ちました')
                print(Fork)


def Ph3():
    while True:

        if Fork[2] == 3 and Fork[3] == 3:
                time.sleep(1)
                print('Ph3が食べ終わりました')
                Fork[2] = 0
                Fork[3] = 0
                print('Ph3がフォークを机に置きました')
                print(Fork)
        elif Fork[2] == 3 and Fork[3] == 0:
                Fork[3] = 3
                print('Ph3が食事を始めました')
                print(Fork)

        elif Fork[2] == 0 and Fork[3] == 3:
                Fork[2] = 3
                print('Ph3が食事を始めました')
                print(Fork)

        elif Fork[2] == 0:
                Waiter(3)
                if counter[2] != 1:
                        Fork[2] = 3
                        print('Ph3が右手にフォークを持ちました')
                print(Fork)

        elif Fork[3] == 0:
                Waiter(3)
                if counter[2] != 1:
                        Fork[3] = 3
                        print('Ph3が左手にフォークを持ちました')
                print(Fork)


def Ph4():
    while True:

        if Fork[3] == 4 and Fork[4] == 4:
                time.sleep(1)
                print('Ph4が食べ終わりました')
                Fork[3] = 0
                Fork[4] = 0
                print('Ph4がフォークを机に置きました')
                print(Fork)

        elif Fork[3] == 4 and Fork[4] == 0:
                Fork[4] = 4
                print('Ph4が食事を始めました')
                print(Fork)

        elif Fork[3] == 0 and Fork[4] == 4:
                Fork[3] = 4
                print('Ph4が食事を始めました')
                print(Fork)

        elif Fork[3] == 0:
                Waiter(4)
                if counter[3] != 1:
                        Fork[3] = 4
                        print('Ph4が右手にフォークを持ちました')
                print(Fork)

        elif Fork[4] == 0:
                Waiter(4)
                if counter[3] != 1:
                        Fork[4] = 4
                        print('Ph4が左手にフォークを持ちました')
                print(Fork)


def Ph5():
    while True:

        if Fork[4] == 5 and Fork[0] == 5:
                time.sleep(1)
                print('Ph5が食べ終わりました')
                Fork[4] = 0
                Fork[0] = 0
                print('Ph5がフォークを机に置きました')
                print(Fork)
        elif Fork[4] == 5 and Fork[0] == 0:
                Fork[0] = 5
                print('Ph5が食事を始めました')
                print(Fork)
        elif Fork[4] == 0 and Fork[0] == 5:
                Fork[4] = 5
                print('Ph5が食事を始めました')
                print(Fork)
        elif Fork[4] == 0:
                Waiter(5)
                if counter[4] != 1:
                        Fork[4] = 5
                        print('Ph5が右手にフォークを持ちました')
                print(Fork)
        elif Fork[0] == 0:
                Waiter(5)
                if counter[4] != 1:
                        Fork[0] = 5
                        print('Ph5が左手にフォークを持ちました')
                print(Fork)


if __name__ == "__main__":
    thread_1 = threading.Thread(target=Ph1)
    thread_2 = threading.Thread(target=Ph2)
    thread_3 = threading.Thread(target=Ph3)
    thread_4 = threading.Thread(target=Ph4)
    thread_5 = threading.Thread(target=Ph5)

    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()