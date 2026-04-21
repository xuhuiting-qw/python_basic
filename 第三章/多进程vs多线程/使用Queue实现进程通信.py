import time
from multiprocessing import Process,Queue


# 子进程1：往队列里放入数据
def test1(q):
    for index in range(5):
        print(f'test1 放入数据:{index}')
        q.put(index)
        time.sleep(0.5)

# 子进程2：往队列里取出数据
def test2(q):
    for index in range(5):
        print(f'test2 取出数据:{q.get()}')
        time.sleep(1)

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=test1,args=(q,))
    p2 = Process(target=test2,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
