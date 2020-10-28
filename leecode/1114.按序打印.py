def printFirst():
    print('first', end='')


def printSecond():
    print('second', end='')


def printThrid():
    print('third', end='')


class Foo:
    def __init__(self):
        self.lock = threading.Lock()

    def first(self, printFirst) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        self.lock.acquire()
        printFirst()
        self.lock.release()

    def second(self, printSecond) -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        self.lock.acquire()
        printSecond()
        self.lock.release()


    def third(self, printThird) -> None:
        # printThird() outputs "third". Do not change or remove this line.
        self.lock.acquire()
        printThird()
        self.lock.release()


import threading

f = Foo()
dict_thread = {1: f.first(), 2: f.second(), 3: f.third()}
sequence_list = [1,2,3]
a = threading.Thread()

initial_thread = [threading.Thread(target=dict_thread[i]) for i in sequence_list]
for i in initial_thread:
    i.start()
for i in initial_thread:
     i.join()
