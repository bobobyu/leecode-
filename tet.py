import multiprocessing as mp
import time

def job(*args):
    for i in args:
        print(i)
        time.sleep(0.1)

p1 = mp.Process(target=job, args=(1, 2, 3))
p2 = mp.Process(target=job, args=(1, 2, 3))
p3 = mp.Process(target=job, args=(1, 2, 3))

p = [p1, p2, p3]
if __name__ == '__main__':
    for i in p:
        i.start()

    for i in p:
        i.join()
