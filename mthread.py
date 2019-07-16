import threading
import time

def cubes():
    for i in range(1,10):
        print("Cubes: {}, {}".format(i,i**3))
        time.sleep(5)

def squares():
    for i in range(1,10):
        print("Square: {}, {}".format(i,i**2))
        time.sleep(5)

if __name__ == '__main__':
    t1 = threading.Thread(target = cubes, args=())
    t2 = threading.Thread(target = squares, args=())
    # cubes()
    # squares()
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(t1.getName())
    print(t2.getName())

    t1.setName('T1')
    t2.setName('T2')

    print(t1.getName())
    print(t2.getName())
    print('Threading count : {}'.format(threading.activeCount()))
    print(t1.is_alive)
    print(t2.is_alive)


    for i in range(1,10):
        print("Main : {}".format(i))
        time.sleep(5)
