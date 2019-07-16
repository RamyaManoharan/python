import multiprocessing
import os
import time

def worker1():
    print("worker1: {}".format(os.getpid()))
    time.sleep(5)

def worker2():
    for i in range(5):
        print("Worker2:{}".format(os.getpid()))
        time.sleep(5)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker1)
    p2 = multiprocessing.Process(target = worker2)

    p1.start()
    p2.start()

    for i in range(5):
        print(os.getpid())

